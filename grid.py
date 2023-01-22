import cv2
from tkinter import *
import numpy as np

def on_trackbar(val):
    global rows, cols
    rows = int(val)
    cols = int(val)

def show_frame():
    _, frame = cap.read()
    for i in range(rows):
        cv2.line(frame, (0, int(i * height/rows)), (int(width), int(i * height/rows)), (255, 255, 255), 2)
    for j in range(cols):
        cv2.line(frame, (int(j * width/cols), 0), (int(j * width/cols), int(height)), (255, 255, 255), 2)

    ret, png = cv2.imencode('.png', frame)
    img = PhotoImage(data=png.tobytes())
    lmain.imgtk = img
    lmain.configure(image=img)
    lmain.after(10, show_frame)

cap = cv2.VideoCapture(0)
width, height = int(cap.get(3)), int(cap.get(4))

root = Tk()
root.title("Grid on Live Video")

lmain = Label(root)
lmain.pack()

rows, cols = 5, 5
slider = Scale(root, from_=5, to=20, orient=HORIZONTAL, command=on_trackbar)
slider.pack()

show_frame()
root.mainloop()