import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.PlyWnd11 = QtWidgets.QLabel(self.centralwidget)
        self.PlyWnd12 = QtWidgets.QLabel(self.centralwidget)
        self.PlyWnd21 = QtWidgets.QLabel(self.centralwidget)
        self.PlyWnd22 = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.PlyWnd11, 1, 1)
        self.gridLayout.addWidget(self.PlyWnd12, 1, 2)
        self.gridLayout.addWidget(self.PlyWnd21, 2, 1)
        self.gridLayout.addWidget(self.PlyWnd22, 2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        # self.cap = cv2.VideoCapture("rtsp://admin:admin123@98.173.8.28:554/cam/realmonitor?channel=2&subtype=1")
