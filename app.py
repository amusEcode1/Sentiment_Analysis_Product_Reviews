!pip install streamlit -q
!pip install joblib -q

from google.colab import drive
drive.mount('/content/drive')

import streamlit as st
import joblib

# Load saved pipeline
@st.cache_resource
def load_model():
    return joblib.load('/content/drive/MyDrive/model.joblib')


model = load_model()

st.title("🛒 Product Review Sentiment Analysis")

review = st.text_area("Enter a product review:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([review])[0]
        st.success(f"Sentiment: **{prediction}**")

!jupyter nbconvert app.ipynb --to py

!jupyter nbconvert --to script "/content/drive/MyDrive/ColabNotebooks/app.ipynb"
