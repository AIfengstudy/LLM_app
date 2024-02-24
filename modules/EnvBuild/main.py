from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from modules.EnvBuild.envBuild_ui import Ui_Form
import fitz
import os
import subprocess


class FirstMainWindow(QWidget,Ui_Form):  # 定义类继承自
    def __init__(self):
        super().__init__()  # 调用父类init方法

        self.setupUi(self)

        self.setWindowTitle("浏览PDF文件")
        # 获取系统桌面分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        # self.resize(self.width-150, self.height-150)
        self.setFixedSize(self.width-180, self.height-130)
        self.uiadd()
        # PDF路径
        # dir_path = os.path.abspath(os.path.dirname(__file__))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_file = os.path.join(dir_path, "pdf\\chatglm3-6b.pdf")
        # 打开PDF文件
        self.doc = fitz.open(dir_file)
        # PDF文档的总页数
        self.page_allnumber = self.doc.page_count-1
        self.setpage_number = 0
        self.image(self.setpage_number)

    def uiadd(self):

        # 设计布局
        self.main_layout = QVBoxLayout(self, spacing=0)  # 窗口的整体布局   下面的水平
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.center_layout = QHBoxLayout()  # 窗口的整体布局  中间的水平
        self.center_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.center_layout)  # 中间
        self.center_layout.addWidget(self.label)
        self.center_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


        #按钮位置
        self.opencmd_btn.setGeometry(QtCore.QRect(int(self.size().width()/2 +150), self.size().height()-25, 0, 0))
        self.back_page_btn.setGeometry(QtCore.QRect(int(self.size().width()/2 +50), self.size().height()-25, 0, 0))
        self.next_page_btn.setGeometry(QtCore.QRect(int(self.size().width()/2 - 50), self.size().height()-25, 0, 0))
        self.previous_page_btn.setGeometry(QtCore.QRect(int(self.size().width()/2 - 150), self.size().height()-25, 0, 0))
        self.home_page_btn.setGeometry(QtCore.QRect(int(self.size().width()/2 - 250), self.size().height()-25, 0, 0))

        self.home_page_btn.setFixedSize(100, 25)
        self.previous_page_btn.setFixedSize(100, 25)
        self.next_page_btn.setFixedSize(100, 25)
        self.back_page_btn.setFixedSize(100, 25)
        self.opencmd_btn.setFixedSize(100, 25)

        self.home_page_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.previous_page_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.next_page_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.back_page_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.opencmd_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.home_page_btn.setEnabled(False)
        self.previous_page_btn.setEnabled(False)
        self.next_page_btn.setEnabled(True)
        self.back_page_btn.setEnabled(True)
        self.opencmd_btn.setEnabled(False)

        # 点击事件
        self.home_page_btn.clicked.connect(self.home_page)
        self.previous_page_btn.clicked.connect(self.previous_page)
        self.next_page_btn.clicked.connect(self.next_page)
        self.back_page_btn.clicked.connect(self.back_page)
        self.opencmd_btn.clicked.connect(self.opencmd_window)


    def home_page(self):
        print('首页')
        self.setpage_number = 0
        self.image(self.setpage_number)
        self.home_page_btn.setEnabled(False)
        self.previous_page_btn.setEnabled(False)
        self.next_page_btn.setEnabled(True)
        self.back_page_btn.setEnabled(True)
        self.opencmd_btn.setEnabled(False)

    def back_page(self):
        print('尾页')
        self.setpage_number = self.page_allnumber
        self.image(self.setpage_number)
        self.home_page_btn.setEnabled(True)
        self.previous_page_btn.setEnabled(True)
        self.next_page_btn.setEnabled(False)
        self.back_page_btn.setEnabled(False)
        self.opencmd_btn.setEnabled(True)

    def previous_page(self):
        print('上一页')
        self.setpage_number = self.setpage_number-1
        self.next_page_btn.setEnabled(True)
        self.back_page_btn.setEnabled(True)
        self.opencmd_btn.setEnabled(False)
        if self.setpage_number ==0:
            self.setpage_number = 0
            self.home_page_btn.setEnabled(False)
            self.previous_page_btn.setEnabled(False)
        self.image(self.setpage_number)

    def next_page(self):
        print('下一页')
        self.setpage_number = self.setpage_number + 1
        self.home_page_btn.setEnabled(True)
        self.previous_page_btn.setEnabled(True)
        if self.setpage_number == self.page_allnumber:
            # self.setpage_number = self.page_allnumber
            self.next_page_btn.setEnabled(False)
            self.back_page_btn.setEnabled(False)
            self.opencmd_btn.setEnabled(True)
        self.image(self.setpage_number)

    # 浏览PDF文件方法
    def image(self, number):
        # 读取一页 0代表第1页
        page_one = self.doc.load_page(number)
        # 将第一页转换为Pixmap
        page_pixmap = page_one.get_pixmap()
        # 将Pixmap转换为QImage
        image_format = QImage.Format_RGBA8888 if page_pixmap.alpha else QImage.Format_RGB888
        page_image = QImage(page_pixmap.samples, page_pixmap.width,page_pixmap.height, page_pixmap.stride, image_format)
        # label的大小设置
        width = page_image.width()
        height = page_image.height()
        # QImage 转为QPixmap
        pix = QPixmap.fromImage(page_image)

        # 设置标签宽和高
        # self.label.setFixedSize(int(width*1.2), int(height*1.2))

        # 设置图片大小自适应标签
        # self.label.setScaledContents(True)
        # 给标签设置图像
        self.label.setPixmap(pix)


    def opencmd_window(self):
        # dir_path = os.path.abspath(os.path.dirname(__file__))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = os.path.join(dir_path, "datasets\\cmd.bat")
        subprocess.call(['cmd', '/c', 'start', '', '/b', bat_path],creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == "__main__":
    app = QApplication([])
    window = FirstMainWindow()
    window.show()
    app.exec()





