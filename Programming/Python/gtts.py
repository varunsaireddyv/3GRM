from gtts import gTTS
from googletrans import Translator
import os
EngText = 'Hello Python and 3grm Group. Hello from the outside At least I can say that I ve triedTo tell you I\'m sorry'
# TelText = "బయటి నుండి హలో కనీసం నేను ప్రయత్నించానని చెప్పగలను మీకు చెప్పడానికి నన్ను క్షమించండి"
translatorDest = 'te'
gTTSLang = 'te'
translatedText = Translator().translate(EngText, dest=translatorDest)
myobj = gTTS(text=translatedText.text, lang=gTTSLang, slow=False)
myobj.save("abc.mp3") 
os.startfile ("abc.mp3")