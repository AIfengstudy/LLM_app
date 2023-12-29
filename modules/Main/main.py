from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from rkwork_ui import  Ui_RKwork
import os
from PyQt5 import QtCore
from PyQt5.QtGui import QFont,QIcon,QPixmap,QCursor
from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QMessageBox,
                             QPushButton,
                             QListWidget,
                             QStackedWidget,
                             QListWidgetItem,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout)


class GzzcaMainwindow(QWidget,Ui_RKwork):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setObjectName('GzzcaMainwindow')
        self.setWindowTitle('众承AI视觉实训软件')

        # 获取桌面信息宽高
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        #控件位置
        self.pushButton.setGeometry(QtCore.QRect(self.width - 60, 30, 40, 40))

        #窗体设置
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(self.width, self.height)
        # 按钮设置
        self.homePag_btn.clicked.connect(self.buttonClick)
        self.envDpl_btn.clicked.connect(self.buttonClick)
        self.dataGen_btn.clicked.connect(self.buttonClick)
        self.modelFtn_btn.clicked.connect(self.buttonClick)
        self.modelTra_btn.clicked.connect(self.buttonClick)
        self.existSys_btn.clicked.connect(self.buttonClick)


    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "homePag_btn":
            self.stackedWidget.setCurrentIndex(0)

        if btnName == "envDpl_btn":
            print('2')

        # SHOW NEW PAGE
        if btnName == "dataGen_btn":
            print('3')

        if btnName == "modelFtn_btn":
            print('4')

        if btnName == 'modelTra_btn':
            pass
        if btnName == "existSys_btn":
            # print("Save BTN clicked!")
            QMessageBox.information(self, "提示", '该功能还未实现', QMessageBox.Yes)





if __name__ == '__main__':
    app = QApplication([])
    window = GzzcaMainwindow()
    window.show()
    app.exec()

