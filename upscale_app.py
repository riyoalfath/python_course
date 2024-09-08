import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("Image Upscaling and Denoising App")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        img = np.array(img)

        if img is None or img.size == 0:
            st.error("Error: Failed to load the image. Please try another one.")
        else:
            st.image(img, caption="Original Image", use_column_width=True)

            denoised_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

            scale_percent = 150  # scale by 150%
            width = int(denoised_img.shape[1] * scale_percent / 100)
            height = int(denoised_img.shape[0] * scale_percent / 100)
            dim = (width, height)
            upscaled_img = cv2.resize(denoised_img, dim, interpolation=cv2.INTER_CUBIC)

            st.image(upscaled_img, caption="Upscaled and Denoised Image", use_column_width=True)

            result = Image.fromarray(upscaled_img)
            st.download_button("Download Processed Image", result.tobytes(), file_name="upscaled_denoised_image.png")
    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.write("Upload an image to start processing.")