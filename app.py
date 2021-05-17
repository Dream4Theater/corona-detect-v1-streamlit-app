import SessionState
import streamlit as st
import tensorflow as tf
import os
import json
import requests
from utils import classes_and_models, update_logger, predict_json

# Setup environment credentials (you'll need to change these)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "covid-test-project-314008-d3dc2b3ab1c0.json" # change for your GCP key
PROJECT = "covid-test-project-314008" # change for your GCP project
REGION = "europe-west1" # change for your GCP region (where your model is hosted)

CLASSES = ['Covid','non-Covid']

CLASSES = classes_and_models["model_1"]["classes"]
MODEL = classes_and_models["model_1"]["model_name"]

### Streamlit code (works as a straigtht-forward script) ###
st.title("Corona Detection")
@st.cache # cache the function so predictions aren't always redone (Streamlit refreshes every click)
def make_prediction(image, model, class_names):
    x = tf.image.decode_png(image, channels=3)
    x = tf.image.resize(x,[128,128])
    x /= 255.
    
    preds = predict_json(project=PROJECT,
                         region=REGION,
                         model=model,
                         instances=x)
    pred_class = class_names[tf.argmax(preds[0])]
    pred_conf = tf.reduce_max(preds[0])
    return image, pred_class, pred_conf

# File uploader allows user to add their own image
uploaded_file = st.file_uploader(label="Upload a corona ct-scan image",
                                 type=["png"])

# Setup session state to remember state of app so refresh isn't always needed
# See: https://discuss.streamlit.io/t/the-button-inside-a-button-seems-to-reset-the-whole-app-why/1051/11 
session_state = SessionState.get(pred_button=False)

# Create logic for app flow
if not uploaded_file:
    st.warning("Please upload an image.")
    st.stop()
else:
    session_state.uploaded_image = uploaded_file.read()
    st.image(session_state.uploaded_image, use_column_width=True)
    pred_button = st.button("Predict")

# Did the user press the predict button?
if pred_button:
    session_state.pred_button = True 

# And if they did...
if session_state.pred_button:
    session_state.image, session_state.pred_class, session_state.pred_conf = make_prediction(session_state.uploaded_image, model=MODEL, class_names=CLASSES)
    st.write(f"Prediction: {session_state.pred_class}, \
               Confidence: {session_state.pred_conf:.1f}")