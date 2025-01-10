# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:54:37 2025

@author: stephv03
"""

# Import libraries
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
import cv2
from  PIL import Image, ImageEnhance
import streamlit as st
#import easyocr
#from pathlib import Path


#def recognize_text(img_path):
#    '''loads an image and recognizes text.'''
#    
#    reader = easyocr.Reader(['en'])
#    return reader.readtext(img_path)


def main():
    
    image = Image.open(r'logo.jpg') #Brand logo image (optional)
    st.set_page_config(layout="wide")
    
    #Create two columns with different width
    col1, col2 = st.columns( [0.7, 0.3])
    with col1:               
        # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Courier New'; color: #959595;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Upload incident report:</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        st.image(image,  width=150)
        
    
    #Add file uploader to allow users to upload photos
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    
    #Add column headings
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        #cwd = Path.cwd()
        #image.save(cwd + '/Images/photo.jpg', 'JPEG')
        
        col1, col2 = st.columns( [0.5, 0.5])
        with col1:
            st.markdown('<p style="text-align: center;">Original</p>',unsafe_allow_html=True)
            st.image(image,width=600)  
    
        with col2:
            st.markdown('<p style="text-align: center;">Text detection output</p>',unsafe_allow_html=True)
            cvImg = image.copy() #cv2.imread(image)
            '''
            # recognize text
            result = recognize_text(cvImg)
            
            for (bbox, text, prob) in result:
                print(f'Detected text: {text} (Probability: {prob:.2f})')
                # get top-left and bottom-right bbox vertices
                (top_left, top_right, bottom_right, bottom_left) = bbox
                top_left = (int(top_left[0]), int(top_left[1]))
                bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

                # create a rectangle for bbox display
                cv2.rectangle(img=cvImg, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)
                '''
                  
            st.image(cvImg, width=600)
    
if __name__ == "__main__":
    main()