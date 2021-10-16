import streamlit as st
from PIL import Image
import numpy as np 
import librosa

import chart_studio.plotly as py
import cufflinks as cf
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

import pickle

cf.go_offline()

import time

import random

# import pandas_profiling
import plotly.graph_objects as go
import plotly
from plotly.subplots import make_subplots

import pandas as pd

class aud_class():
    st.set_page_config(layout='wide')
    def main(self):
        # d=st.sidebar.selectbox("Audio Samples",('Audio 1','Audio 2','Audio 3','Audio 4','Audio 5','Audio 6'),)

        c1,c2=st.columns([2,2])
        with c1:
            image = Image.open("ai4lyf.png")
            st.image(image, width = 200)
        with c2:
            st.header('AI ENGINE')

        self.progressbar()

        st.subheader('Play Audio Sample')

        st.markdown("----------------------------------------------------------------------------------------------------------------------------------")

        # audc='/home/bigpenguin/code/audio_samples/224_1b1_Tc_sc_Meditron_healthy.wav'
        auds=st.sidebar.file_uploader("Upload a file", type=("wav"))
        print(auds)
        if auds:
            self.audio_class(auds)
            
 
    def audio_class(self,audc):
        
        data_x, sampling_rate = librosa.load(audc,res_type='kaiser_fast')
        mfccs = np.mean(librosa.feature.mfcc(y=data_x, sr=sampling_rate, n_mfcc=40).T,axis=0)

        sample=np.reshape(mfccs,(1,mfccs.size))
        sample=pd.DataFrame([mfccs])
        st.audio(audc)
        # sam=st.expander('Audio sample')
        # sam.write(st.write(audc))

        st.markdown("----------------------------------------------------------------------------------------------------------------------------------")

        aib=st.button('AI Engine')
        if aib:
            self.model(sample,audc,data_x)

    def model(self,sample,audc,data_x):
        with open('rf_emo.pkl', 'rb') as file:  
            rf = pickle.load(file)

        pred=rf.predict(sample)

        self.label(audc)
        num = random.randint(1, 5)
        with st.spinner('Predicting with AI Engine...'):
            time.sleep(num)
        st.success('Finished Successfully')

        predd=pd.DataFrame([pred],columns=['prediction'])

        fig=px.line(data_x,title='Audio Frequency Sample',labels={'value':'Frequency(dB)','index':'Instances'},width=950,height=550)
        st.plotly_chart(fig)
            
        expander=st.expander('Diagnosis by AI Engine')
        expander.write(predd)

    def label(self,auds):
        df=pd.read_csv('emotions_labels.csv')
        lab=auds.name
        
        # print(lab)
        dlab=df[df['id']==lab]['status']
        print(dlab)
        expander=st.sidebar.expander('Labeled by Experts')
        expander.write(dlab)
    
    def progressbar(self):
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            bar.progress(i + 1)
            time.sleep(0.01)
        st.write('\n')

        

obj=aud_class()
obj.main()

