from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200
ypos = 200
width = 300
height = 300


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Application Name")

    win.show()
    sys.exit(app.exec_()


window()
