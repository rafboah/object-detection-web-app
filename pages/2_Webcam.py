import streamlit as st
from ultralytics import YOLO
from detect_objects import process_webcam


st.set_page_config(page_title="Webcam", page_icon="🎥")


def display_form(model_objects):
    with st.form("my_form"):
        selected_objects = st.multiselect('Choose objects to detect', model_objects, default=['person']) 
        min_confidence = st.slider('Confidence score', 0.0, 1.0, 0.5)
        webcam_access = st.form_submit_button('Enable Webcam 🎥')
        return selected_objects, min_confidence, webcam_access


def detect_webcam_objects():
    model = YOLO('yolov8n.pt')
    object_names = list(model.names.values())

    selected_objects, min_confidence, webcam_access = display_form(model_objects=object_names)
    if webcam_access:
        process_webcam(selected_objects, min_confidence, model)


detect_webcam_objects()