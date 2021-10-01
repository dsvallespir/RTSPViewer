
import sys
from PyQt5.QtWidgets import QMessageBox, QAction, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QMutex, QWaitCondition
from PyQt5.QtGui import QImage, QPixmap

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        print("Dialog")

    def initUI(self):
        self.vlayout = QVBoxLayout(self)
        self.hlay_ip = QHBoxLayout(self)
        self.hlay_user = QHBoxLayout(self)
        self.hlay_pass = QHBoxLayout(self)
        self.hlay_port = QHBoxLayout(self)
        self.hlay_stream = QHBoxLayout(self)
        self.hlay_buttons = QHBoxLayout(self)

        self.vlayout.addLayout(self.hlay_ip)
        self.vlayout.addLayout(self.hlay_user)
        self.vlayout.addLayout(self.hlay_pass)
        self.vlayout.addLayout(self.hlay_port)
        self.vlayout.addLayout(self.hlay_stream)
        self.vlayout.addLayout(self.hlay_buttons)

        self.lbl_ip = QLabel("Ip: ", self,)
        self.lbl_user = QLabel("User: ", self)
        self.lbl_pass = QLabel("Pass: ", self)
        self.lbl_port = QLabel("Port: ", self)
        self.lbl_stream_type = QLabel("Stream type: ", self)

        self.lbl_user.setFixedWidth(50)
        self.lbl_user.setAlignment(Qt.AlignRight)
        self.lbl_pass.setFixedWidth(50)
        self.lbl_pass.setAlignment(Qt.AlignRight)
       #self.lbl_pass.setTextFormat()
        self.lbl_port.setFixedWidth(50)
        self.lbl_port.setAlignment(Qt.AlignRight)
        self.lbl_ip.setFixedWidth(50)
        self.lbl_ip.setAlignment(Qt.AlignRight)
        self.lbl_stream_type.setFixedWidth(70)
        self.lbl_stream_type.setAlignment(Qt.AlignRight)

        self.btn_ok = QPushButton("Ok")
        self.btn_ok.clicked.connect(self.handle_ok_button)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.handle_cancel_button)

        self.hlay_ip.addWidget(self.lbl_ip);
        self.hlay_user.addWidget(self.lbl_user);
        self.hlay_pass.addWidget(self.lbl_pass);
        self.hlay_port.addWidget(self.lbl_port);
        self.hlay_stream.addWidget(self.lbl_stream_type);
        self.hlay_buttons.addWidget(self.btn_ok)
        self.hlay_buttons.addWidget(self.btn_cancel)

        self.lne_user = QLineEdit(self)
        self.lne_pass = QLineEdit(self)
        self.lne_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.lne_ip = QLineEdit(self)
        #self.lne_ip.setInputMask("000.000.000.000;_")
        self.lne_port = QLineEdit(self)
        self.cmbox_stream = QComboBox(self)
        self.cmbox_stream.addItem("main stream")
        self.cmbox_stream.addItem("sub stream")

        self.hlay_ip.addWidget(self.lne_ip)
        self.hlay_user.addWidget(self.lne_user)
        self.hlay_pass.addWidget(self.lne_pass)
        self.hlay_port.addWidget(self.lne_port)
        self.hlay_stream.addWidget(self.cmbox_stream)
        self.setFixedHeight(200)
        self.setFixedWidth(200)

        self.setTabOrder(self.lne_ip, self.lne_user)
        self.setTabOrder(self.lne_user, self.lne_pass)
        self.setTabOrder(self.lne_pass, self.lne_port)
        self.setTabOrder(self.lne_port, self.cmbox_stream)
        self.setTabOrder(self.cmbox_stream, self.btn_ok)
        self.setTabOrder(self.btn_ok, self.btn_cancel)

    def handle_ok_button(self):
        print(self.lbl_ip.text() + self.lne_ip.text())
        print(self.lbl_user.text() + self.lne_user.text())
        print(self.lbl_pass.text() + self.lne_pass.text())
        print(self.lbl_port.text() + self.lne_port.text())
        print(self.lbl_stream_type.text() + self.get_stream())
        self.close()

    def handle_cancel_button(self):
        exit(0)

    def get_ip(self):
        return self.lne_ip.text()

    def get_user(self):
        return self.lne_user.text()

    def get_pass(self):
        return self.lne_pass.text()

    def get_port(self):
        return self.lne_port.text()

    def get_stream(self):
        if str(self.cmbox_stream.currentText())=="main stream":
            return "1"
        else:
            return "2"