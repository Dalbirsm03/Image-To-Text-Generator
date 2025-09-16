import PIL
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.title("GEMINI APP")
input = st.text_input('Input', key='input')
upload_file = st.file_uploader("Choose an image....", type=["jpg", "png", "jpeg"])

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


submit = st.button("Ask The Question")

if submit:
    response = get_gemini_response(input, image)
    st.subheader('The Response is ...')
    st.write(response)



