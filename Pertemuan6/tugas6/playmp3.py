from playsound import playsound
import tkinter as tk
from tkinter import ttk

def play_mp3():
    playsound('tugas6/Gunslinger.mp3')

app = tk.Tk()
app.title("MP3 Player")

button = ttk.Button(app, text="Play MP3", command=play_mp3)
button.pack(padx=20, pady=20)

app.mainloop()