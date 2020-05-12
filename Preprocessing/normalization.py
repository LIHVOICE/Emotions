#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import re
import numpy as np
import pydub
from pydub import AudioSegment
from pydub import effects
from pydub.effects import normalize

folder = 'audio_emotion'
for  fichier_audio in os.listdir(folder): # for each element in the audio folder
    folder_path = os.path.join(folder, fichier_audio) # path of each item  in the audio folder
   
    
    if(os.path.isdir(folder_path)):
        #print(folder_path)
        audios = os.listdir(folder_path)
        for audio_file in audios:
            if not audio_file.endswith('norm.wav'):
                
            
            #print(audio_file)
                
                begin_file = re.split("\.", audio_file)
                _sound = AudioSegment.from_file(folder_path+'/'+audio_file, "wav")
                sound = effects.normalize(_sound) #Normalize sound
                sound.export(folder_path+'/'+begin_file[0]+'_norm.wav', format="wav") #export a new normalize file

