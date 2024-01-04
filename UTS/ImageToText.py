from PIL import Image, ImageTk
from pytesseract import pytesseract
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def lakukan_ocr():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    
    path_to_image = 'UTS/picture/images.jpg'

    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img)

    result_label.config(text=text)

app = tk.Tk()
app.title("Mengubah Gambar menjadi Teks")

button = ttk.Button(app, text="Play Program", command=lakukan_ocr)
button.pack(padx=20, pady=20)

result_label = ttk.Label(app, text="Sugianto Tegar Samudra 220511162")
result_label.pack()

app.mainloop()