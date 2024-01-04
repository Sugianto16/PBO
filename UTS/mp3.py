import os
import pygame
import tkinter as tk
from tkinter import ttk

def play_mp3():
    pygame.mixer.init()
    pygame.mixer.music.load('UTS/music/Gunslinger.mp3')
    pygame.mixer.music.play()

def stop_mp3():
    pygame.mixer.music.stop()

app = tk.Tk()
app.title("MP3 Player")

# Mengatur latar belakang tkinter
app.configure(bg='lightblue')


# Menambahkan tombol play
play_button = ttk.Button(app, text="Play MP3", command=play_mp3)
play_button.pack(pady=20)

# Menambahkan tombol stop
stop_button = ttk.Button(app, text="Stop", command=stop_mp3)
stop_button.pack(pady=20)

app.mainloop()