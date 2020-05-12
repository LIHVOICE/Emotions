#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import numpy as np
import librosa
import wavio
import ffmpeg
import logmmse
from logmmse import logmmse_from_file

folder = 'audio_emotion'
for  fichier_audio in os.listdir(folder): # for each element in the audio folder
    folder_path = os.path.join(folder, fichier_audio) # path of each item  in the audio folder
    if(os.path.isdir(folder_path)):
        audios = os.listdir(folder_path)
        for audio_file in audios:
            if audio_file.endswith('norm.wav'):
                begin_file = re.split("\.", audio_file)
                r = wavio.read(folder_path+'/'+audio_file) #read audio file with wavio for the rate
                y,sr = librosa.load(folder_path+'/'+audio_file) #load audio with librosa
                logmmse.logmmse(y, r.rate, output_file = folder_path+'/'+begin_file[0]+'_outNoise.wav') #reduceNoise

