# import cv2
import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

def display_info():
    st.header('Object Detection Web App 📸')
    st.subheader('Powered by YOLOv8')
    st.subheader('Welcome 👋')
    st.write(
            """
            This project is a web-based object detection application 
             powered by YOLOv8 and built with Streamlit. It enables users 
             to upload videos and detect objects in real-time, leveraging 
             the cutting-edge capabilities of the YOLO (You Only Look Once) 
             deep learning model for object detection tasks. This app aims 
             to provide a user-friendly interface for object detection, making 
             it accessible to users without deep technical knowledge in deep 
             learning or computer vision.

             This project enables users to upload videos, select objects to detect,
             and a choose a mininum confidence level for detection. Also, users are able to
             detect objects in live feed via their webcam. 

             Currently, due to Streamlit's limitation and certain restrictions, this
             web app doesn't function as expected. This web app is to showcase this project,
             and also enable users to play around with it as this site is still under
             construction. Users can also clone the github repository and work with the
             Object Detection App on their local machines.
             """
    )
                    

if __name__ == "__main__":
    display_info()