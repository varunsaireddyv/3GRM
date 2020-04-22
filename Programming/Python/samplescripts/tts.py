import numpy as np
import wavio
import soundfile as sf

AUDIO_FILE = "C:\\Users\\padma\\Desktop\\ans_01.wav"

data, fs = sf.read("ans_01.wav", dtype='float32')
sd.play(data, fs)

rate = 22050  # samples per second
T = 3         # sample duration (seconds)
f = 440.0     # sound frequency (Hz)
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
wavio.write("ans_01.waw", x, rate, sampwidth=3)


#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 
import os
import wavio
  
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
# wavio.write(AUDIO_FILE, data, fs ,sampwidth=2)
with sr.AudioFile(AUDIO_FILE) as source: 
    #reads the audio file. Here we use record instead of 
    #listen 
    audio = r.record(source)   
  
try: 
    print("The audio file contains: " + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
