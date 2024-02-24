from PyQt5 import QtCore
from PyQt5.QtGui import *
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


class GzzcaMainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('GzzcaMainwindow')
        self.setWindowTitle('众承AI视觉实训软件')



        # 获取桌面信息宽高
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # 设置布局
        self.main_layout = QVBoxLayout(self, spacing=0)  # 窗口的整体布局 主体垂直布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局  上边的水平
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.center_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局  中间的垂直
        self.center_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局   下面的水平
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addLayout(self.bottom_layout)

        # 定义top_layout对象
        self.top_label_widget = QLabel(self)  # 上边框图片
        self.top_label_widget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.top_label_widget.setFixedHeight(100)  # 设置控件高度
        self.top_label_widget.setPixmap(QPixmap("./images/topbg.png").scaled(self.width + 10, 100))
        self.top_label_widget.setScaledContents(True)
        self.top_layout.addWidget(self.top_label_widget)

        # 定义bottom_layout对象
        bottom_font = QFont()
        bottom_font.setFamily("楷体")
        bottom_font.setPointSize(16)
        bottom_font.setBold(True)

        self.bottom_label_widget = QLabel(self)
        self.bottom_label_widget.setFixedHeight(30)
        self.bottom_label_widget.setFont(bottom_font)
        self.bottom_label_widget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.bottom_label_widget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.bottom_label_widget.setStyleSheet(
            "QLabel{border-image: url(images/bottombg.png);color:white;font:bold 16px;}")
        self.bottom_label_widget.setText('版权所有：广东众承人工智能研究有限公司')
        self.bottom_layout.addWidget(self.bottom_label_widget)

        # 左侧功能菜单栏UI
        with open('pyqss/gzc_QLeftWidget.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.left_style = f.read()
        self.left_widget = QListWidget()
        self.left_widget.setStyleSheet(self.left_style)
        self.center_layout.addWidget(self.left_widget)

        # 右侧功能显示栏UI
        with open('pyqss/gzc_QRightWidget.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.right_style = f.read()
        self.right_widget = QStackedWidget()
        self.right_widget.setStyleSheet(self.right_style)
        self.center_layout.addWidget(self.right_widget)

        self._setup_ui()

    def _setup_ui(self):
        # 设置窗体无边框
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # 设置窗体自适应左面
        self.resize(self.width, self.height)
        # self.setFixedSize(self.width, self.height)

        # 设置退出按钮
        self.button_close = QPushButton(self)
        self.button_close.setFixedSize(40, 40)
        self.button_close.setGeometry(QtCore.QRect(self.width - 60, 30, 20, 20))
        self.button_close.setStyleSheet("QPushButton{border-image: url(images/logout.png)}")  # 设置背景图片，设置后一直存在

        self.button_close.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.clicked.connect(self.exit_button)  # 退出

        # 设置最小化按钮 并没有在主页面上显示 可删除
        self.minimize_window = QPushButton(self)
        self.minimize_window.setFixedSize(40, 40)
        self.minimize_window.setGeometry(QtCore.QRect(self.width - 120, 30, 50, 50))
        self.minimize_window.setStyleSheet("QPushButton{border-image: url(images/prev.png)}")  # 设置背景图片，设置后一直存在
        self.minimize_window.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_window.clicked.connect(self.minimize_button)  # 最小化事件
        self.minimize_window.setVisible(False)  # 隐藏

        # 顶部文字图                                                                                      # 关于在窗口中自定义一个标签部件
        self.top_logo_widget = QLabel(self)                                                             # 传参定义
        self.top_logo_widget.setFixedSize(500, 70)                                                      # 大小设置
        self.top_logo_widget.setGeometry(QtCore.QRect(10, 10, 0, 0))                                    # 位置设置
        self.top_logo_widget.setPixmap(QPixmap("./images/logo_title.png").scaled(500, 70))              # 背景设置
        self.top_logo_widget.setScaledContents(True)                                                    # 自适应设置

        # 设置软件窗口图标
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("./images/logos.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.icon)

        # 左侧QlistWidget 设置
        self.left_widget.setCursor(QtCore.Qt.PointingHandCursor)  # 鼠标变手型
        self.left_widget.setIconSize(QtCore.QSize(25, 25))  # list中图标大小

        self.left_widget.itemClicked.connect(self.exit_system)  # 点击左侧退出系统
        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)  # 点击左侧按钮触发事件 qlistwidget 自带索引
        self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏横向滚动条
        self.left_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏纵向滚动条

        list_str = ['软件首页', '环境部署', '制数据集', '模型微调', '模型实训', '退出系统']
        url_pic = ['ico01.png', 'ico02.png', 'ico03.png', 'ico04.png', 'ico05.png', 'ico07.png']

        for i in range(6):
            url_icon = QIcon("./images/icon/" + url_pic[i])
            url_item = list_str[i]
            # 左侧选项的添加
            self.items = QListWidgetItem(url_icon, url_item, self.left_widget)  # 先定义内容，后装入qlistwidgetItem
            self.items.setSizeHint(QtCore.QSize(30, 60))
            self.items.setTextAlignment(QtCore.Qt.AlignVCenter)  # 居中显示
            # 渲染内容
            self.listwidgetFuns(url_item)

    def listwidgetFuns(self, item):

        if item == '软件首页':
            right_index_label = QLabel()
            right_index_label.setGeometry(QtCore.QRect(0, 0, 0, 0))
            # self.right_index_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            right_index_label.setPixmap(
                QPixmap("./images/center_index.png").scaledToWidth(self.width - 100).scaledToHeight(self.height - 130))
            right_index_label.setScaledContents(True)
            right_index_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.right_widget.addWidget(right_index_label)

        elif item == '环境部署':
            print('环境部署')
            from EnvBuild.main import MainWindow
            self.firstwindow = MainWindow()
            self.right_widget.addWidget(self.firstwindow)

        elif item == '制数据集':
            print('制数据集')
            from DataMake.main import MainWindow  # 需要调整下 rc文件的导入方式
            self.secondwindow = MainWindow()
            self.right_widget.addWidget(self.secondwindow)

        elif item == '模型微调':
            print('模型微调')
            from FineTuning.main import MainWindow
            self.thirdWindow = MainWindow()
            self.right_widget.addWidget(self.thirdWindow)


        elif item == '模型实训':
            print('模型实训')
            from Traing.main import MainWindow
            self.fourthWindow = MainWindow()
            self.right_widget.addWidget(self.fourthWindow)

        else:
            print(item)

    # 窗口中退出系统
    def exit_button(self):
        yes_close = QMessageBox.question(self, '广东众承人工智能研究有限公司', '你确定要退出软件吗?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if yes_close == QMessageBox.Yes:
            q_exit = QApplication.instance()
            q_exit.quit()  # 关闭窗口
        else:
            return

    # 左侧菜单中退出系统
    def exit_system(self, item):
        if item.text() == '退出系统':
            yes_close = QMessageBox.question(self, '广东众承人工智能研究有限公司', '你确定要退出软件吗?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if yes_close == QMessageBox.Yes:
                q_exit = QApplication.instance()
                q_exit.quit()  # 关闭窗口
            else:
                return
        else:
            return

    # 最小化和最大化窗体
    def minimize_button(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    gzc_main = GzzcaMainwindow()
    gzc_main.show()
    app.exec()
