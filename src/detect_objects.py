import cv2
import streamlit as st


def process_video(input_path, selected_objects, min_confidence, model):
    if input_path is not None:
        video_stream = cv2.VideoCapture(input_path)
        width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)) 
        height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        fourcc = cv2.VideoWriter_fourcc(*'h264') 
        fps = int(video_stream.get(cv2.CAP_PROP_FPS))
        output_path = input_path.split('.')[0] + '_output.mp4' 
        out_video = cv2.VideoWriter(output_path, int(fourcc), fps, (width, height))
        
        with st.spinner('Processing video...'):
            total_frames = int(video_stream.get(cv2.CAP_PROP_FRAME_COUNT))
            progress_bar  = st.progress(0)
            frame_count = 0

            while True:
                ret, frame = video_stream.read()

                if not ret:
                    break

                result = model(frame)

                for detection in result[0].boxes.data:
                    x0, y0 = (int(detection[0]), int(detection[1]))
                    x1, y1 = (int(detection[2]), int(detection[3]))
                    score = round(float(detection[4]), 2)
                    cls = int(detection[5])
                    object_name =  model.names[cls]
                    label = f'{object_name} {score}'

                    if model.names[cls] in selected_objects and score > min_confidence:
                        cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
                        cv2.putText(frame, label, (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                detections = result[0].verbose()
                cv2.putText(frame, detections, (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  
                out_video.write(frame)

                frame_count += 1
                progress = int((frame_count / total_frames) * 100)
                progress_bar.progress(progress, f'{progress}% Processed')

        video_stream.release()
        out_video.release()

        return output_path
    
    else:
        return None

def process_webcam(selected_objects, min_confidence, model):
    # Start the webcam
    webcam = cv2.VideoCapture(0)

    width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # framewidth = 640
    # frameheight = 480

    # cap.set(3, framewidth)
    # cap.set(4, frameheight)

    while True:
        # Read a frame from the webcam
        ret, frame = webcam.read()

        if not ret:
            break

        # Perform object detection
        results = model(frame)

        # Draw the detection results on the frame
        for detection in results[0].boxes.data:
                    x0, y0 = (int(detection[0]), int(detection[1]))
                    x1, y1 = (int(detection[2]), int(detection[3]))
                    score = round(float(detection[4]), 2)
                    cls = int(detection[5])
                    object_name =  model.names[cls]
                    label = f'{object_name} {score}'

                    if model.names[cls] in selected_objects and score > min_confidence:
                        cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
                        cv2.putText(frame, label, (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
        detections = results[0].verbose()
        cv2.putText(frame, detections, (10, 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Object Detection', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    webcam.release()
    cv2.destroyAllWindows()