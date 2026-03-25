import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap

img = "/img"


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Test PyQt5')
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel('<h1>PyQt5 działa!</h1>', parent=window)
    helloMsg.move(60, 15)

    window.show()

    # 2. Uruchomienie pętli zdarzeń
    sys.exit(app.exec_())

main()