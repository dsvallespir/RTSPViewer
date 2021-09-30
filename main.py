# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap

user = "DNA"
passw = "DNA2020!"
ip = "98.173.8.28"
port = "8830"
stream_type = "1"
rtsp_stream_prefix = "rtsp://" + user + ":" + passw + '@' + ip + ":" + port + "/cam/realmonitor?channel="
rtsp_stream_suffix = "&subtype=" + stream_type


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.setupUi(self)

        self.gridLayout = QGridLayout(self)


        self.PlyWnd11 = QLabel(self)
        self.PlyWnd12 = QLabel(self)
        self.PlyWnd21 = QLabel(self)
        self.PlyWnd22 = QLabel(self)

        self.gridLayout.addWidget(self.PlyWnd11,1,1)
        self.gridLayout.addWidget(self.PlyWnd12, 1, 2)
        self.gridLayout.addWidget(self.PlyWnd21, 2, 1)
        self.gridLayout.addWidget(self.PlyWnd22, 2, 2)

        #self.setCentralWidget(self.gridLayout)

        # Impresión de prueba
        # print(rtsp_stream_prefix + "1" + rtsp_stream_suffix)

        self.cap = cv2.VideoCapture()

        self.cap11 = cv2.VideoCapture(rtsp_stream_prefix + "1" + rtsp_stream_suffix)
        self.cap12 = cv2.VideoCapture(rtsp_stream_prefix + "2" + rtsp_stream_suffix)
        self.cap21 = cv2.VideoCapture(rtsp_stream_prefix + "3" + rtsp_stream_suffix)
        self.cap22 = cv2.VideoCapture(rtsp_stream_prefix + "4" + rtsp_stream_suffix)

        i = 0
        self.show()
        # app.aboutToQuit.connect(self.closeEvent)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(finish)

        while True:
            if i == 0:
                self.cap = self.cap11
                i = 1
            elif i == 1:
                self.cap = self.cap12
                i = 2
            elif i == 2:
                self.cap = self.cap21
                i = 3
            elif i == 3:
                self.cap = self.cap22
                i = 0
            ret, frame = self.cap.read()

            if not ret:
                break

            self.img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.p = QPixmap.fromImage(self.img)
            self.p = self.p.scaled(600, 300, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

            if i == 0:  self.PlyWnd11.setPixmap(self.p)
            elif i == 1: self.PlyWnd12.setPixmap(self.p)
            elif i == 2: self.PlyWnd21.setPixmap(self.p)
            elif i == 3: self.PlyWnd22.setPixmap(self.p)

    def closeEvent(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.cap.release()
            self.cap11.release()
            self.cap12.release()
            self.cap21.release()
            self.cap22.release()
            cv2.destroyAllWindows()
        else:
            event.ignore()

    # def keyPressEvent(self, event):
    #    if event.key() == QtCore.Qt.Key_Q:
    #        print("Killing")
    #        self.deleteLater()
    #    elif event.key() == QtCore.Qt.Key_Enter:
    #        self.proceed()
    #    event.accept()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    #a.show()
    sys.exit(app.exec_())