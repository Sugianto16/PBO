import cv2
import tkinter as tk
from tkinter import ttk

def play_video():
    cap = cv2.VideoCapture('tugas6/ForRevenge.mp4')
    
    if not cap.isOpened():
        print("Error opening video file")

    def update_frame():
        ret, frame = cap.read()
        if ret:
            _, frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), cv2.resize(frame, (640, 480))
            photo = tk.PhotoImage(data=cv2.imencode('.ppm', frame)[1].tobytes())
            label.config(image=photo)
            label.image = photo
            label.after(10, update_frame)
        else:
            cap.release()

    update_frame()

app = tk.Tk()
app.title("OpenCV Video Player")

button = ttk.Button(app, text="Play Video", command=play_video)
button.pack(padx=20, pady=20)

label = ttk.Label(app)
label.pack()

app.mainloop()
