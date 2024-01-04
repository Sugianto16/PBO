import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

#Create tkinter object
app = tk.Tk()

#Atur Ukuran Window
app.geometry("450x450")

#Tambahkan Judul
app.title("Kalkulator Luas dan Keliling")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

app.mainloop()