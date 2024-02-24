import time
for i in range(100):
	print(i)
	time.sleep(0.1)


# 九九乘法表
#for i in range(1, 10):
#    for j in range(1, i+1):
#        print(f'{j}x{i}={i*j}\t', end='')
#    print()

#
# from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow
# from PyQt5.QtCore import pyqtSignal
# import sys
#
# class MyTextEdit(QTextEdit):
#     clicked = pyqtSignal()
#
#     def mousePressEvent(self, event):
#         super().mousePressEvent(event)
#         self.clicked.emit()
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.text_edit = MyTextEdit(self)
#         self.setCentralWidget(self.text_edit)
#
#         self.text_edit.clicked.connect(self.on_text_edit_clicked)
#
#     def on_text_edit_clicked(self):
#         print("TextEdit被点击了")
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction
# from PyQt5.QtGui import QFont
#
# app = QApplication([])
# window = QMainWindow()
#
# menu_bar = QMenuBar(window)
# font = QFont("Arial", 12)  # 设置字体为Arial，大小为12
# menu_bar.setFont(font)
#
# action = QAction("菜单项", window)
# menu_bar.addAction(action)
#
# window.setMenuBar(menu_bar)
# window.show()
