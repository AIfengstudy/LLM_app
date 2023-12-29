import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QSplitter,QApplication,QPushButton,QLabel,QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import *


class LoginwinWidget(QWidget):
    def __init__(self):
        super(LoginwinWidget, self).__init__()
        # 获取根目录地址
        # self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.dir_path = os.path.abspath('')

        self.setupUi()
        self.Use_Qss()

    def setupUi(self):
    # MySignal = pyqtSignal(str)

        # 设置 窗口无边框和背景透明 *必须
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window) #无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)#透明
        # self.setWindowOpacity(0.9)  #透明
        self.setObjectName("登录")
        self.resize(577, 361)
        self.setStyleSheet("QWidget{border-radius:15px}")
        # self.setStyleSheet(
        #     """background:rgb(255, 255, 0);
        #     border-top-left-radius:{0}px;
        #     border-bottom-left-radius:{0}px;
        #     border-top-right-radius:{0}px;
        #     border-bottom-right-radius:{0}px;""".format(50)
        # )

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("external_files/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("")

        self.textEdit_1 = QtWidgets.QLineEdit(self)
        self.textEdit_1.setGeometry(QtCore.QRect(170, 150, 261, 41))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_1.setPlaceholderText('请输入账号')
        self.textEdit_1.setStyleSheet("QLineEdit{font-size:12px;color:gray;padding:5;font:bold 13px;border-radius: 5px;}")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(110, 160, 54, 21))
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet(
            "QLabel{box-shadow: 1px 1px 3px;font-size:15px;border-radius:15px;font-family: 微软雅黑;}")

        self.textEdit_2 = QtWidgets.QLineEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 210, 261, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit_2.setPlaceholderText('请输入密码')
        self.textEdit_2.setStyleSheet("QLineEdit{font-size:12px;color:gray;padding:5;font:bold 13px;border-radius: 5px;}")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(110, 220, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{box-shadow: 1px 1px 3px;font-size:15px;border-radius:15px;font-family: 微软雅黑;}")

        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.setFixedSize(150, 40)
        self.login_btn.setGeometry(QtCore.QRect(110, 280, 151, 41))
        self.login_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setStyleSheet("QPushButton{\n"
                                    "background:green;\n"
                                    "color:white;\n"
                                    "box-shadow: 1px 1px 3px;font-size:18px;border-radius:15px;font-family: 微软雅黑;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background:black;\n"
                                    "}")

        self.exit_btn = QtWidgets.QPushButton(self)
        self.exit_btn.setFixedSize(150, 40)
        self.exit_btn.setGeometry(QtCore.QRect(282, 280, 151, 41))
        self.exit_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setStyleSheet("QPushButton{\n"
                                        "background:#CE0000;\n"
                                        "color:white;\n"
                                        "box-shadow: 1px 1px 3px;font-size:18px;border-radius: 15px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background:black;\n"
                                        "}")

        self.botton_close = QtWidgets.QPushButton(self)
        self.botton_close.setGeometry(QtCore.QRect(540, 6, 31, 31))
        self.botton_close.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.botton_close.setText("")
        self.botton_close.setObjectName("label_close")
        self.botton_close.setVisible(False) #隐藏关闭按钮

        self.top_logo_widget = QLabel(self)
        self.top_logo_widget.setFixedSize(60, 60)
        self.top_logo_widget.setGeometry(QtCore.QRect(80, 45, 441, 51))
        self.top_logo_widget.setPixmap(QPixmap("external_files/images/logo.png").scaled(500, 80))
        self.top_logo_widget.setScaledContents(True)

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(150, 50, 441, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(85, 170, 255);\n"
"color: rgb(0, 85, 127);")
        self.label_title.setObjectName("label_title")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "登录窗口"))
        self.label_1.setText(_translate("Form", "账  号："))
        self.label_2.setText(_translate("Form", "密  码："))
        self.login_btn.setText(_translate("Form", "登录"))
        self.exit_btn.setText(_translate("Form", "关闭"))
        self.label_title.setText(_translate("Form", "众承AI大语言实训软件"))

    def Use_Qss(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("external_files/images/login_index.png")))
        self.setPalette(palette)
        self.botton_close.setStyleSheet("QPushButton{border-image: url(images/close.png)}")
        self.botton_close.clicked.connect(self.exit_button)  # 退出
        self.exit_btn.clicked.connect(self.exit_button)  # 退出
        self.login_btn.clicked.connect(self.login_button)  # 登录

    def login_button(self):
        try:
            user = self.textEdit_1.text()  # QLineEdit获取值方式
            pwd = self.textEdit_2.text()
            if len(user) == 0:
                QMessageBox.information(self, "广东众承人工智能研究有限公司", '请输入账号!', QMessageBox.Yes)
                return
            if len(pwd) == 0:
                QMessageBox.information(self, "广东众承人工智能研究有限公司", '请输入密码!', QMessageBox.Yes)
                return
            self.close()
            # QMessageBox.information(self, "广东众承人工智能研究有限公司", self.dir_path, QMessageBox.Yes)
            from gzc_main import MainTabWidget
            self.main_Window = MainTabWidget()
            self.main_Window.show()

            # subprocess.Popen("python main.py")

        except:
            QMessageBox.information(self, "广东众承人工智能研究有限公司", '登录异常!', QMessageBox.Yes)
            return

    def exit_button(self):
        q_exit = QApplication.instance()
        q_exit.quit()  # 关闭窗口


def main():
    app = QApplication(sys.argv)
    main_wnd = LoginwinWidget()
    main_wnd.show()
    app.exec()


if __name__ == '__main__':
    main()
