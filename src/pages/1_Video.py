import streamlit as st
from ultralytics import YOLO
from detect_objects import process_video
from save_video import save_video


st.set_page_config(page_title="Video", page_icon="📸")


def display_form(model_objects):
    with st.form("Video Upload"):
        uploaded_video = st.file_uploader("Upload video", type=['mp4'])
        selected_objects = st.multiselect('Choose objects to detect', model_objects, default=['person']) 
        min_confidence = st.slider('Confidence score', 0.0, 1.0, 0.5)
        st.form_submit_button('Upload ⬆️')
        return uploaded_video, selected_objects, min_confidence


def video():
    model = YOLO('yolov8n.pt')
    object_names = list(model.names.values())

    uploaded_video, selected_objects, min_confidence = display_form(object_names)
    if uploaded_video:
        detect_clicked = st.button("Detect 🔍")
            
        if detect_clicked:
            input_path = save_video(uploaded_video)

            if input_path:
                output_path = process_video(input_path, selected_objects, min_confidence, model)

                if output_path:
                    st.success(body="Video Processing Complete", icon="✅")
                    st.balloons()
                    st.video(output_path)


video()