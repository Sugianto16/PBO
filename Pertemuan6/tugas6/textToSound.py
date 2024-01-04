from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk

def teks_ke_suara():
    mytext = 'Sugianto Tegar Samudra'
    language = 'id'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("sugianto.mp3")
    playsound("sugianto.mp3", True)

app = tk.Tk()
app.title("Text-to-Speech dan Pemutar Audio")

button = ttk.Button(app, text="Teks ke Suara dan Putar Audio", command=teks_ke_suara)
button.pack(padx=20, pady=20)

app.mainloop()
