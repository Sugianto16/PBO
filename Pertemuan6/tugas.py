import cv2
from PIL import Image, ImageTk
from pytesseract import pytesseract
from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class AplikasiOCR:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengolahan Multimedia")
        
        # Frame untuk setiap aplikasi
        self.frame_video = ttk.Frame(root)
        self.frame_mp3 = ttk.Frame(root)
        self.frame_teks_suara = ttk.Frame(root)
        self.frame_ocr = ttk.Frame(root)

        # Tombol untuk setiap aplikasi
        self.btn_putar_video = ttk.Button(self.frame_video, text="Putar Video", command=self.putar_video)
        self.btn_putar_mp3 = ttk.Button(self.frame_mp3, text="Putar MP3", command=self.putar_mp3)
        self.btn_teks_suara = ttk.Button(self.frame_teks_suara, text="Teks ke Suara", command=self.teks_ke_suara)
        self.btn_lakukan_ocr = ttk.Button(self.frame_ocr, text="Lakukan OCR", command=self.lakukan_ocr)

        # Setup UI untuk setiap aplikasi
        self.setup_video()
        self.setup_mp3()
        self.setup_teks_suara()
        self.setup_ocr()

        # Menampilkan aplikasi pertama secara default
        self.frame_video.pack()

    def setup_video(self):
        self.btn_putar_video.pack(padx=20, pady=20)

    def putar_video(self):
        self.frame_video.pack_forget()
        cap = cv2.VideoCapture('tugas6/ForRevenge.mp4')
        
        if not cap.isOpened():
            print("Error membuka file video")

        def update_frame():
            ret, frame = cap.read()
            if ret:
                _, frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), cv2.resize(frame, (640, 480))
                photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                label.config(image=photo)
                label.image = photo
                label.after(10, update_frame)
            else:
                cap.release()
                self.frame_video.pack()

        label = ttk.Label(self.frame_video)
        label.pack()
        update_frame()

    def setup_mp3(self):
        self.btn_putar_mp3.pack(padx=20, pady=20)

    def putar_mp3(self):
        self.frame_mp3.pack_forget()
        playsound('tugas6/Gunslinger.mp3')
        self.frame_mp3.pack()

    def setup_teks_suara(self):
        self.btn_teks_suara.pack(padx=20, pady=20)

    def teks_ke_suara(self):
        self.frame_teks_suara.pack_forget()
        mytext = 'Sugianto Tegar Samudra'
        language = 'id'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("sugianto.mp3")
        playsound("sugianto.mp3", True)
        self.frame_teks_suara.pack()

    def setup_ocr(self):
        self.btn_lakukan_ocr.pack(padx=20, pady=20)

    def lakukan_ocr(self):
        self.frame_ocr.pack_forget()
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path_to_tesseract
        
        path_to_image = filedialog.askopenfilename()

        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)

        result_label = ttk.Label(self.frame_ocr, text=text)
        result_label.pack()
        self.frame_ocr.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiOCR(root)
    root.mainloop()
