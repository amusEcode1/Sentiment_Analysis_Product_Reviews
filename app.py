import streamlit as st
import joblib

# Load saved pipeline
@st.cache_resource
def load_model():
    return joblib.load('model.joblib')

model = load_model()

st.title("🛒 Product Review Sentiment Analysis")

review = st.text_area("Enter a product review:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([review])[0]

        # Set background color based on prediction
        if prediction.lower() == 'positive':
            color = "#d4edda"  # light green
            text_color = "#155724"
        else:
            color = "#f8d7da"  # light red
            text_color = "#721c24"

        st.markdown(
            f"<div style='background-color: {color}; color: {text_color}; padding: 15px; border-radius: 5px;'>"
            f"<h4>Sentiment: {prediction}</h4>"
            f"</div>",
            unsafe_allow_html=True
        )
