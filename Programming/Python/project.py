from gtts import gTTs
import speach_recognisation as sr
import os
import sntplib
import webbrowser

def talktome(audio):
	print(audio)
	tts=gtts(text=audio ,lang='en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3') 
	
#listens commands

def mycommand():
	
	r=sr.reconizer()
	
	with sr.microphone() as sourse:
		print('I am, ready for your next command')
		r.pause_threshhold = 1
		#r.adjust_for_ambient_noise(sorce.doration=1)
		audio=r.listen(source)
		
		try:
			command=r.recognize_google(audio)
			print('You said' + mycommand)
			
		#loop back
		except sr.UnknownValueError:
			assitant(mycommand())
			
			return command
			
#if staments
def assistant(command):
	
	if 'Open youtube'in command:
		chrome_path='/user/bin/google-chrome'
		url='https://www.youtube.com'
		webbrowser.get(chrome_path).open(url)
		
		if 'What\'s upp' in command:
			talktome('Chilln bro')
		if 'email' in command:
			talktome('Who is the recipient')
			recipient=mycommand()
			
			if 'Varun' in recipient:
				talktome('What should I say')
				content=mycommand()
	
#init gmail smtp
mail=smtplib.SMTP('smtp.gmail.com', 587)

#identify the server

mail.ehlo

#encrypt seesion
mail.starttls()
#login
mail.login('username=varunbillas@gmail.com' ,'password=orangefruit')

#sends message
mail.sendmail('Varun' ,'varunbillas@gmail.com' ,content)

#close connection
mail.close

talktome('Email has been sent')

talktome('I am ready for your next command')

while True:
	assistant(mycommand())
