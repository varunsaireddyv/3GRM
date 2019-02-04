from gtts import gTTs
import speach_recognisation as sr
import os
import sntplib
import webbrowser

def talktome(audio):
	print(audio)
	tts=gTTs(Text=audio. lang = 'en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3') 
	
#listens commands

def mycommand():
	
	r=sr.reconiser()
	
	with sr.microphone() as sourse:
		print('I am, ready for your next command')
		r.pause_threshhold = 1
		r.adjust_for_ambient_noise(sorce.doration=1)
		audio=r.listening
