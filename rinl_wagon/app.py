
import streamlit as st #web app and camera
import numpy as np # for image processing 
from PIL import Image #Image processing 
import cv2 #computer vision 

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("PencilSketcher App - updated streamlit camera 📷 module")
st.write("This Web App is to help convert your photos to realistic Pencil Sketches")

# collect the user input 

#file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

# collecting the input image from user camera 

file_image = st.camera_input(label = "Take a pic of you to be sketched out")

if file_image:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)
    if st.button("Download Sketch Images"):
        im_pil = Image.fromarray(final_sketch)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')
   

else:
     st.write("You haven't uploaded any image file")
   

st.write("Courtesy: 1littlecoder Youtube Channel - [Sketch Code](https://github.com/amrrs/youtube-r-snippets/blob/master/Create_a_Pencil_Sketch_Portrait_with_Python_OpenCV.ipynb)")