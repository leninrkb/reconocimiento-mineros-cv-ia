import tkinter as tk

import torch as torch
from PIL import Image, ImageTk
import cv2
import imutils


#Interfaz
ventana = tk.Tk()
ventana.geometry("994x699+200+10")
ventana.title("Interfaz")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="camara.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

video = None

def video_stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

def iniciar():
    global video
    ret, frame = video.read()

    if ret == True:
        frame = imutils.resize(frame, width=491, height=900)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=img)
        etiq_video.configure(image=image)
        etiq_video.image = image
        etiq_video.after(9, iniciar)
    else:
        etiq_video.image = ""
        video.release()

def quitar():
    global video
    #etiq_video.place_forget()
    video.release()

#Color
fondo_boton = "#FFF"


#BOTONES
boton = tk.Button(ventana, text="INICIAR", bg=fondo_boton, relief="flat",
                  cursor="hand2", command=video_stream, width=15, height=2, font=("Calisto MT", 12, "bold"))
boton.place(x=165, y=590)

boton2 = tk.Button(ventana, text="APAGAR", bg=fondo_boton, relief="flat",
                  cursor="hand2", command=quitar, width=15, height=2, font=("Calisto MT", 12, "bold"))
boton2.place(x=665, y=590)

#Etiqueta
etiq_video = tk.Label(ventana, bg="black")
etiq_video.place(x=247, y=119)


ventana.mainloop()
