import streamlit as st
from PIL import Image
import numpy as np 

import time

import random


import pandas as pd


class moke():

    st.set_page_config(layout='wide')

    def main(self):
        c1,c2=st.columns([2,2])
        with c1:
            image = Image.open("ai4lyf.png")
            st.image(image, width = 200)
        with c2:
            st.header('AI ENGINE')

        self.progressbar()

        st.subheader('Play Audio Sample')

        st.markdown("----------------------------------------------------------------------------------------------------------------------------------")

        auds=st.sidebar.selectbox('Select Audio',('Audio 1','Audio 2','Audio 3','Audio 4','Audio 5','Audio 6','Audio 7'))

        
        if auds=='Audio 1':
            self.audio_class('calm.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("calm1.png")
                st.image(image)

        if auds=='Audio 2':
            self.audio_class('happy.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("happy1.png")
                st.image(image)
        
        if auds=='Audio 3':
            self.audio_class('sad.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("sad1.png")
                st.image(image)

        if auds=='Audio 4':
            self.audio_class('angry.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("angry1.png")
                st.image(image)

        if auds=='Audio 5':
            self.audio_class('fearful.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("fearful1.png")
                st.image(image)

        if auds=='Audio 6':
            self.audio_class('disgust.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("disgust1.png")
                st.image(image)

        if auds=='Audio 7':
            self.audio_class('surprise.wav')
            self.ai_wf()
            with st.expander("AI Diagnosis"):
                image = Image.open("surprise1.png")
                st.image(image)




    
        # with st.expander("Audio Features & Models"):
        #     image = Image.open("Capture.PNG")
        #     st.image(image)

        
    def ai_wf(self):
        with st.expander("AI Workflow"):
            image = Image.open("arch1.png")
            st.image(image,width=1200,use_column_width=True)
        

    def audio_class(self,audc):
        
        # data_x, sampling_rate = librosa.load(audc,res_type='kaiser_fast')
        # mfccs = np.mean(librosa.feature.mfcc(y=data_x, sr=sampling_rate, n_mfcc=40).T,axis=0)

        # sample=np.reshape(mfccs,(1,mfccs.size))
        # sample=pd.DataFrame([mfccs])
        st.audio(audc)

        # expander=st.expander('Biomarkers')
        # expander.write(st.image(image))

        # if auds=='Audio':
        #     diagnosis()


    def progressbar(self):
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            bar.progress(i + 1)
            time.sleep(0.01)
        st.write('\n')

obj=moke()
obj.main()

