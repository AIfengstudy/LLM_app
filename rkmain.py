import os
from rkwork_ui import Ui_RKwork
from modules.EnvBuild.main import FirstMainWindow
from modules.DataMake.main import SecondMainWindow
from modules.FineTuning.main import ThirdMainWindow
from modules.Traing.main import ForthMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication,
                             QMessageBox,
                             QWidget,
                             )


class GzzcaMainwindow(QWidget, Ui_RKwork):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setObjectName('GzzcaMainwindow')
        self.setWindowTitle('众承AI视觉实训软件')
        # 全局变量
        work_pth = os.getcwd()
        ico_pth = os.path.join(work_pth, 'external_files/images/logos.png')
        work_dir = self.make_dir()

        # 获取桌面信息宽高
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # 控件位置
        self.close_btn.setGeometry(QtCore.QRect(self.width - 60, 30, 40, 40))

        # 窗体设置
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(self.width, self.height)
        # 按钮设置
        self.homePag_btn.clicked.connect(self.button_click)
        self.envDpl_btn.clicked.connect(self.button_click)
        self.dataGen_btn.clicked.connect(self.button_click)
        self.modelFtn_btn.clicked.connect(self.button_click)
        self.modelTra_btn.clicked.connect(self.button_click)
        self.existSys_btn.clicked.connect(self.button_click)
        self.close_btn.clicked.connect(self.button_click)

        # 添加页面
        self.first_window = FirstMainWindow()
        self.stackedWidget.addWidget(self.first_window)
        self.second_window = SecondMainWindow()
        self.stackedWidget.addWidget(self.second_window)
        self.third_window = ThirdMainWindow()
        self.stackedWidget.addWidget(self.third_window)
        self.fourth_window = ForthMainWindow()
        self.stackedWidget.addWidget(self.fourth_window)
        # 窗体图标
        self.icon = QIcon(ico_pth)
        self.setWindowIcon(self.icon)

    def button_click(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "homePag_btn":
            self.stackedWidget.setCurrentIndex(0)

        if btnName == "envDpl_btn":
            self.stackedWidget.setCurrentIndex(1)

        if btnName == "dataGen_btn":
            self.stackedWidget.setCurrentIndex(2)

        if btnName == "modelFtn_btn":
            self.stackedWidget.setCurrentIndex(3)

        if btnName == 'modelTra_btn':
            self.stackedWidget.setCurrentIndex(4)

        if btnName == "existSys_btn" or btnName == "close_btn":
            yes_close = QMessageBox.question(self, '广东众承人工智能研究有限公司', '你确定要退出软件吗?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if yes_close == QMessageBox.Yes:
                exit = QApplication.instance()
                exit.quit()
            else:
                return

    # 工作路径 有一个返回值
    def make_dir(self):
        import os
        from pathlib import Path
        try:
            desktop_path = Path.home() / "Desktop"
            work_dir = os.path.join(desktop_path, 'GZZC_LLM')

            if os.path.exists(work_dir):
                return work_dir
            else:
                os.makedirs(work_dir)
                return work_dir
        except:
            print('创建失败')


if __name__ == '__main__':
    app = QApplication([])
    window = GzzcaMainwindow()
    window.show()
    app.exec()

