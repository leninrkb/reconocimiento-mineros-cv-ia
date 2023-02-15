import tkinter as tk
import subprocess
import torch as torch
from PIL import Image, ImageTk
import cv2
import imutils

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from app_escritorio.visualizarPdf import visualizarImprimirExportar
app = QApplication(sys.argv)


#Interfaz
ventana = tk.Tk()
ventana.geometry("1241x600+200+10")
ventana.title("Interfaz")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

# Crear la entrada de texto
entry = tk.Entry(ventana, cursor="hand2", width=38)
entry.config(font=('Helvetica', 15))
entry.place(x=664, y=210)


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr

def mostrar_datos():
    # Crear una instancia de la clase MiClase
    mi_clase =  visualizarImprimirExportar()

    # Mostrar la ventana
    mi_clase.show()

    # Iniciar la aplicación
    sys.exit(app.exec_())

#Color
fondo_boton = "#FFF"


#BOTONES
# Crear una función lambda que llame a la función con los parámetros
my_lambda = lambda: run_command("python detect.py")

boton = tk.Button(ventana, text="INGRESAR", bg=fondo_boton, relief="flat",
                  cursor="hand2", command=my_lambda, width=35, height=2, font=("Calisto MT", 15, "bold"))
boton.place(x=664, y=344)

boton1 = tk.Button(ventana, text="REPORTES", bg=fondo_boton, relief="flat",
                  cursor="hand2", command=mostrar_datos, width=35, height=2, font=("Calisto MT", 15, "bold"))
boton1.place(x=664, y=503)



ventana.mainloop()