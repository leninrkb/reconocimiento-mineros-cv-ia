import sys
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import date
from datetime import datetime
import mysql.connector

# Abrir la cámara
cap = cv2.VideoCapture(0)

cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='proyecto_mineros'
)

class Ventana(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl_imagen = QLabel(self)
        self.lbl_imagen.setGeometry(0, 0, 640, 480)
        self.lbl_imagen.setScaledContents(True)



        self.btn_foto = QPushButton('Tomar Foto', self)
        # self.btn_foto.move(0, 485)             
        self.btn_foto.setGeometry(QtCore.QRect(0, 485, 131, 51))
        self.btn_foto.setStyleSheet("background-color: lightgreen;\n"
"border-radius: 10px;")
        self.btn_foto.clicked.connect(self.tomar_foto)

        self.setWindowTitle('Cámara')
        self.setGeometry(100, 100, 640, 600)

        self.timer = cv2.createBackgroundSubtractorMOG2()

        self.show()

    def tomar_foto(self):
        ret, frame = cap.read()

        carpeta = "img/"

        today = str(date.today())
        dt = datetime.now()
        hour = str(dt.hour)
        minut =str( dt.minute)
        seconds = str(dt.second)
        microseconds= str(dt.microsecond)

        extencion = ".jpg"
        PATH=carpeta+today+'-'+hour+minut+seconds+microseconds+extencion
        cv2.imwrite(carpeta+today+'-'+hour+minut+seconds+microseconds+extencion, frame)

        cursor = cnx.cursor()

        # Insertar una fila en la tabla "personas"
        query = "INSERT INTO registro_empleado (CED_EMP, FECHA_ENTRADA, CASCO, CHALECO, BOTAS, OBSERVACION, IMAGEN_NOMBRE, PATH) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
        values = ("1804567891", dt, "1", "1", "1", "ninguna", "nombre", PATH)
        cursor.execute(query, values)

        cnx.commit()

        print("Foto tomada")

    def start_webcam(self):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        height, width, channel = frame.shape
        step = channel * width
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)

        self.lbl_imagen.setPixmap(QPixmap.fromImage(qImg))

    def closeEvent(self, event):
        cap.release()
        sys.exit()

app = QApplication(sys.argv)
ventana = Ventana()

while True:
    ventana.start_webcam()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cursor.close()
cnx.close()

sys.exit(app.exec_())
