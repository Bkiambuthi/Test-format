import streamlit as st
from PIL import Image

# Function to inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Custom CSS styles
local_css("style.css")

# Page title
st.title("Rice Grain Classification")

# Subtitle
st.subheader("An AI-based approach to classify different types of rice grains")

# Display an image in the center column
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    st.image("https://example.com/your-image.jpg", use_column_width=True)  # Replace with your image URL or path

with col3:
    st.write("")

# Section for uploading an image
st.write("## Upload an Image")
uploaded_file = st.file_uploader("Choose a rice grain image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Add a button for prediction
    if st.button('Classify Image'):
        # Call your prediction function here
        # result = your_prediction_function(image)
        # st.write(f"Prediction: {result}")
        st.write("This is where the prediction result will be shown.")

    st.write("Adjust the confidence threshold:")
    confidence_threshold = st.slider('Confidence Threshold', 0.0, 1.0, 0.5)

# Additional sections
st.markdown("## Features of Our Classifier")
st.write("""
- **Accuracy**: Our model is highly accurate with an accuracy rate of over 95%.
- **Speed**: Fast classification results.
- **User-friendly**: Easy to use interface.
""")

# Adding a logo
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://example.com/your-logo.png" alt="Logo" width="100">
    </div>
    """,
    unsafe_allow_html=True
)
