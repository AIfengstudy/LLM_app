import os
from modules.DataMake.datamake_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QFont, QIcon


class SecondMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pushButton_2.clicked.connect(self.makedataset)
        self.lineEdit_2.returnPressed.connect(self.makedataset)
        self.pushButton_3.clicked.connect(self.deleText)
        self.pushButton.clicked.connect(self.export)
    #  删除数据集

    def deleText(self):
        if os.path.isfile('cache.json'):
            with open('cache.json', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                lines = lines[:-5]
            with open('cache.json', 'w',encoding='utf-8') as f:
                f.writelines(lines)
                f.flush()
            self.showText()

            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            QMessageBox.warning(self, '提示', '删除失败，无数据存在')

    #   制作数据集代码
    def makedataset(self):  # makedataset ————> showText
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '':
            QMessageBox.warning(self, '提示', '生成失败，请输入问题或答案！')
        else:
            instruction = self.lineEdit.text()
            output = self.lineEdit_2.text()
            data = '''{{
        "instruction": "{}",
        "input": "",
        "output": "{}"
    }},'''.format(instruction, output)

            print(data)
            with open('cache.json', 'a',encoding= 'utf-8') as f:
                f.write(data + '\n')
            self.showText()


#   显示数据集代码
    def showText(self):

        with open('cache.json','r',encoding='utf-8') as f:
            text = f.read()
            self.plainTextEdit.setPlainText(text)

        self.lineEdit.clear()
        self.lineEdit_2.clear()


#   导出数据集代码
    def export(self):
        try:
            if  not os.path.isfile('cache.json'):
                QMessageBox.warning(self, '提示', '导出失败，无数据集！')
                return
            else:
                file_path = QFileDialog.getExistingDirectory(self, '选择导出文件位置')

                if  file_path:
                    #设置文件保存位置
                    filename = "data.json"
                    filepath = file_path + "/" + filename
                    # cache————> data————>清空缓存
                    with open('cache.json','r+',encoding='utf-8') as f:
                          content = f.read()[:-2] # 删除末尾字符
                          f.seek(0, 0)
                          f.write('[\n')
                          f.write(content)
                          f.write('\n]')
                          f.flush()

                    import shutil

                    with open('data.json', 'w',encoding='utf-8') as f:
                        f.truncate(0)

                    with open('cache.json', 'r',encoding='utf-8') as source:
                        with open('data.json', 'w',encoding='utf-8') as target:
                            shutil.copyfileobj(source, target)

                    #   学生选择数据集保存路径


                    with open('data.json', 'r',encoding='utf-8') as source:
                        with open(filepath, 'w',encoding='utf-8') as target:
                            shutil.copyfileobj(source, target)

                    QMessageBox.information(self, "众承大语言模型实训APP", "导出成功", QMessageBox.Ok)   #写个方法 用于弹出信息提示
                    self.plainTextEdit.clear()
                    os.remove('cache.json')

                else:
                    QMessageBox.information(self, "众承大语言模型实训APP", "导出失败，未选择路径", QMessageBox.Ok)

        except:
            print('导出失败！')




if __name__ == '__main__':
    app = QApplication([])
    window = SecondMainWindow()
    window.show()
    app.exec()

