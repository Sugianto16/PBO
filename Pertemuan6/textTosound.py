from gtts import gTTS 
from playsound import playsound

mytext = 'Sugianto Tegar Samudra'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("sugianto.mp3") 
playsound("sugianto.mp3", True)