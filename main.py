
import cv2
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QMutex, QWaitCondition
from PyQt5.QtGui import QImage, QPixmap

from dialog import MyDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.cap = cv2.VideoCapture(rtsp_stream_prefix + "1" + rtsp_stream_suffix)

        self.dlg = MyDialog()
        self.dlg.exec_()
        self.login()
        self.initUI()
        self.menu()

        self.cap = self.ch1
        print("App configurada")

        if not self.cap.isOpened():
            print("no se pudo abrir la cámara")
            exit()

        iterador = 0

        while True:
            if iterador == 0:
                self.cap = self.ch1
            if iterador == 1:
                self.cap = self.ch2
            if iterador == 2:
                self.cap = self.ch3
            if iterador == 3:
                self.cap = self.ch4

            ret, frame = self.cap.read()

            if not ret:
                print("no se pudo recibir vieo")
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #cv2.imshow("frame", rgb)
            convert = QImage(rgb.data, rgb.shape[1], rgb.shape[0], QImage.Format_RGB888)
            p = convert.scaled(320, 240, Qt.IgnoreAspectRatio)

            keyboard = cv2.waitKey(0)
            if cv2.waitKey(1) == ord('q'):
                print("Saliendo..")
                break

            if iterador == 0:
                self.label_11.setPixmap(QPixmap.fromImage(p))
                iterador = 1
                continue
            if iterador == 1:
                self.label_12.setPixmap(QPixmap.fromImage(p))
                iterador = 2
                continue
            if iterador == 2:
                self.label_21.setPixmap(QPixmap.fromImage(p))
                iterador = 3
                continue
            if iterador == 3:
                self.label_22.setPixmap(QPixmap.fromImage(p))
                iterador = 0

        self.cap.release()
        cv2.destroyAllWindows()

    def closeEvent(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.cap.release()
            self.ch1.release()
            self.ch2.release()
            self.ch3.release()
            self.ch4.release()
            cv2.destroyAllWindows()
            print("Saliendo..")
            self.dlg.destroy()
            exit(0)
            event.accept()
        else:
            event.ignore()

    def login(self):

        user = self.dlg.get_user()
        passw = self.dlg.get_pass()
        ip = self.dlg.get_ip()
        port = self.dlg.get_port()
        stream_type = self.dlg.get_stream()
        #stream_type = "1"

        rtsp_stream_prefix = "rtsp://" + user + ":" + passw + '@' + ip + ":" + port + "/cam/realmonitor?channel="
        rtsp_stream_suffix = "&subtype=" + stream_type

        #print(rtsp_stream_prefix + "1" + rtsp_stream_suffix))
        self.ch1 = cv2.VideoCapture(rtsp_stream_prefix + "1" + rtsp_stream_suffix)
        self.ch2 = cv2.VideoCapture(rtsp_stream_prefix + "2" + rtsp_stream_suffix)
        self.ch3 = cv2.VideoCapture(rtsp_stream_prefix + "3" + rtsp_stream_suffix)
        self.ch4 = cv2.VideoCapture(rtsp_stream_prefix + "4" + rtsp_stream_suffix)

    def initUI(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.grid = QGridLayout(self.centralwidget)
        self.label_11 = QLabel(self)
        self.label_12 = QLabel(self)
        self.label_21 = QLabel(self)
        self.label_22 = QLabel(self)
        self.label_11.resize(320, 240)
        self.label_12.resize(320, 240)
        self.label_21.resize(320, 240)
        self.label_22.resize(320, 240)
        self.grid.addWidget(self.label_11, 0, 0)
        self.grid.addWidget(self.label_12, 0, 1)
        self.grid.addWidget(self.label_21, 1, 0)
        self.grid.addWidget(self.label_22, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.show()

    def menu(self):
        quit_ = QAction("Quit", self)
        quit_.triggered.connect(self.closeEvent)

        about_ = QAction("About", self)
        about_.triggered.connect(self.about_event)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(quit_)
        file_menu.addAction(about_)

    def about_event(self):
        QMessageBox.about(self, "About RTSPViewer", "Sebastián Vallespir 2021")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    #a.show()
    app.exec_()
