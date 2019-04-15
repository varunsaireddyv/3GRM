from gtts import gTTS
import os

tts=gTTS(text="Hello Varun. Both are great",lang="en")
tts.save("Sample.mp3")
os.system("Sample.mp3")

