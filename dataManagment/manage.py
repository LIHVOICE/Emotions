#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil

#Creation of folders which will contain the audios according to the emotions

path = './'

#Creation of a first folder in which the audios will be classified
nouveau_dossier = 'audio_emotion'
if not os.path.exists(nouveau_dossier):
    os.makedirs(nouveau_dossier)

#creation of folders for each emotion

#neutral
neutral = (nouveau_dossier+'/'+"neutral")
if not os.path.exists(neutral):
    os.makedirs(neutral)   
#calm    
calm = (nouveau_dossier+'/'+"calm")
if not os.path.exists(calm):
    os.makedirs(calm)
#happy
happy = (nouveau_dossier+'/'+"happy")
if not os.path.exists(happy):
    os.makedirs(happy)
#sad    
sad = (nouveau_dossier+'/'+"sad")
if not os.path.exists(sad):
    os.makedirs(sad)
#angry
angry = (nouveau_dossier+'/'+"angry")
if not os.path.exists(angry):
    os.makedirs(angry)
#fearfull   
fearfull = (nouveau_dossier+'/'+"fearfull")
if not os.path.exists(fearfull):
    os.makedirs(fearfull)
#disgust    
disgust = (nouveau_dossier+'/'+"disgust")
if not os.path.exists(disgust):
    os.makedirs(disgust)
#surprised
surprised = (nouveau_dossier+'/'+"surprised")
if not os.path.exists(surprised):
    os.makedirs(surprised)


#use of dictionarry
#creation of dictionaries with for key, the number corresponding to the column of the emotion (dico1) 

dico1 = {"1":"neutral", "2":"calm", "3":"happy", "4":"sad", "5":"angry", "6":"fearfull", "7":"disgust", "8":"surprised"}
#file and audio browsing and copy of each audio file
for actor in os.listdir(path):
    if os.path.isdir(actor) and actor[0] == 'A':
        for audio in os.listdir(actor):
            shutil.copy(actor+'/'+audio, nouveau_dossier+'/'+dico1[audio[7]])
          

