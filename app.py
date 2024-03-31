# import cv2
# import streamlit as st
# from ultralytics import YOLO

# def app():
#     st.header('Object Detection Web App')
#     st.subheader('Powered by YOLOv8')
#     st.write('Welcome!')
#     model = YOLO('yolov8n.pt')
#     object_names = list(model.names.values())

#     with st.form("my_form"):
#         uploaded_file = st.file_uploader("Upload video", type=['mp4'])
#         selected_objects = st.multiselect('Choose objects to detect', object_names, default=['person']) 
#         min_confidence = st.slider('Confidence score', 0.0, 1.0)
#         st.form_submit_button(label='Submit')
            
#     if uploaded_file is not None: 
#         input_path = uploaded_file.name
#         file_binary = uploaded_file.read()
#         with open(input_path, "wb") as temp_file:
#             temp_file.write(file_binary)
#         video_stream = cv2.VideoCapture(input_path)
#         width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)) 
#         height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
#         fourcc = cv2.VideoWriter_fourcc(*'h264') 
#         fps = int(video_stream.get(cv2.CAP_PROP_FPS)) 
#         output_path = input_path.split('.')[0] + '_output.mp4' 
#         out_video = cv2.VideoWriter(output_path, int(fourcc), fps, (width, height)) 

#         with st.spinner('Processing video...'): 
#             while True:
#                 ret, frame = video_stream.read()
#                 if not ret:
#                     break
#                 result = model(frame)
#                 for detection in result[0].boxes.data:
#                     x0, y0 = (int(detection[0]), int(detection[1]))
#                     x1, y1 = (int(detection[2]), int(detection[3]))
#                     score = round(float(detection[4]), 2)
#                     cls = int(detection[5])
#                     object_name =  model.names[cls]
#                     label = f'{object_name} {score}'

#                     if model.names[cls] in selected_objects and score > min_confidence:
#                         cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
#                         cv2.putText(frame, label, (x0, y0 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
#                 detections = result[0].verbose()
#                 cv2.putText(frame, detections, (10, 10),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#                 # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
#                 out_video.write(frame) 
#             video_stream.release()
#             out_video.release()
#         st.video(output_path)

# if __name__ == "__main__":
#     app()

import cv2
from ultralytics import YOLO

def detect_webcam_objects():
    # Load the pre-trained YOLO model
    model = YOLO('yolov8n.pt')

    # Start the webcam
    cap = cv2.VideoCapture(0)

    framewidth = 640
    frameheight = 480

    cap.set(3, framewidth)
    cap.set(4, frameheight)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

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
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_webcam_objects()