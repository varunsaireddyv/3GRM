from gtts import gTTs
import speach_recognisation as sr
import os
import sntplib
import webbrowser

def talktome(audio):
	print(audio)
	tts=gTTs(Text=audio. lang='en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3') 
	
#listens commands

def mycommand():
	
	r=sr.reconizer()
	
	with sr.microphone() as sourse:
		print('I am, ready for your next command')
		r.pause_threshhold = 1
		r.adjust_for_ambient_noise(sorce.doration=1)
		audio=r.listen(source)
		
		try:
			command=r.recognize_google(audio)
			print('You said' + command)= '/n'
			
#loop back

except sr.UnknownValueError:
	assitant(mycommand())
	
	return command
	
#if staments
def assistant(command):
	
	if 'open email'in command:
		chrome_path='/user/bin/google-chrome'
		url='https://www.email.com/r/python'
		webbrowser.get(chrome_path).open(url)
		
		if 'What\'s upp' im command:
			talktome('Chilln bro')
		if 'email' in command:
			talktome('Who is the recipiant')
			recipient=mycommand()
			
			if 'rajesh ,bhumi ,varun' in recipien:
				talktome('What should I say')
				content=mycommand()
