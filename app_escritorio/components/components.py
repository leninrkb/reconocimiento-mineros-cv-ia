from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class ReporteImg(QLabel):

    def __init__(self, img_path):
        super().__init__()

        self.img = QPixmap(img_path).scaledToWidth(200)
        self.setPixmap(self.img)