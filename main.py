import sys
from cProfile import label

import cv2
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from classes.generate_dates_to_learn import LineGenerator

img = "/img"


# image = imageLoader("img/squre.jpg")
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.button =QPushButton('Load Image', self)
        self.button.clicked.connect(self.get_folder)
        self.labelImage = QLabel(self)
        self.textEditor = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.labelImage)
        layout.addWidget(self.textEditor)
        self.setLayout(layout)

    def get_folder(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'open file', r"", "Image files (*.jpg *.png *.jpeg)"
        )
        if file_name:
            self.imageLoader(file_name)

    def imageLoader(self, path):
        img = cv2.imread(path)
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, channel = img.shape
            bytes_per_line = 3 * width
            q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            # print(img.shape)
            self.img_info = QLabel(f"Informacje: {img.shape}", self)
            self.layout().addWidget(self.img_info)
            pixmap = QPixmap.fromImage(q_img)
            self.labelImage.setPixmap(pixmap.scaled(self.labelImage.size(), aspectRatioMode=1))


def showUI():
    app = QApplication(sys.argv)
    main = window()
    main.show()
    sys.exit(app.exec_())

def main():

    line = LineGenerator()
    for i in range(100):
        line.create_sample("img")
        print(i)
    showUI()

main()