import streamlit as st
import pandas as pd
import mediapipe as mp
import numpy as np
import tempfile
import cv2
import time
from PIL import Image

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
DEMO_IMAGE = './assets/site_image/book.png'
DEMO_VIDEO = 'demo.mp4'

st.title('A Sign Language Interpreter')
st.write("Here's our first attempt at using data to create a table:")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
    width:350px
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
    width:350px
    margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title('ASLi')
st.sidebar.subheader('parameters')


@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = width/float(w)
        dim = (int(w*r), height)
    else:
        r = width/float(w)
        dim = (width, int(h*r))

    #resize karne ko
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


app_mode = st.sidebar.selectbox('Choose the App Mode',
                                ['About App', 'Run on Image', 'Run on Video']
                                )

if app_mode == 'About App':
    st.markdown('In this Application we are using **MediaPipe** for creating a FaceMesh App. ')
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width:350px
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width:350px
        margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.video('https://youtu.be/T8SQ8T0iKVs?si=DyUU-O-FanFwbFWo')
    st.markdown(
        '''
        About Us\n
        '''
    )
elif app_mode == 'Run on Image':
    drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1)
    st.sidebar.markdown('---')

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width:350px
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width:350px
        margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("**Detected Faces**")
    kpi1_text = st.markdown("0")

    max_faces = st.sidebar.number_input('Maximum Number of faces', value=2, min_value=1)
    st.sidebar.markdown('---')
    detection_confidence = st.sidebar.slider('Min Detection Confidence', min_value=0.0, max_value=1.0, value=0.5)
    st.sidebar.markdown('---')

    img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=['jpeg','jpg','png'])
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))

    st.sidebar.text('Original Image')
    st.sidebar.image(image)









































