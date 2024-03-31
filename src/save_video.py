import streamlit as st

def save_video(uploaded_video):
    if uploaded_video is not None: 
        input_path = uploaded_video.name
        file_binary = uploaded_video.read()

        try:
            with open(input_path, "wb") as temp_file:
                temp_file.write(file_binary)
                
        except IOError:
            st.error(body="An error occurred", icon="❌")
            print("IOError: Video save error")
            return None
        
        print("Success: Video saved successfully.")
        return input_path
    
    else:
        st.warning(body="Please upload a video", icon="⚠️")
        return None