import streamlit as st
import cv2
import numpy as np
from PIL import Image
import torch


st.title("Virtual Try-On")
st.write("Capture your image using the camera:")
person_image = st.camera_input("Take a picture")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    