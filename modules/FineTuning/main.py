import json
import os
import shutil
import subprocess
from pathlib import Path
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QHeaderView, QTreeWidgetItem, QFileDialog, QMessageBox
from modules.FineTuning.fine_Tuning_ui import Ui_Form


class ThirdMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # 模型显示位置初始设置
        self.treeWidget.setHeaderLabels(["文件名", "文件类型"])
        self.treeWidget.setColumnCount(2)
        self.treeWidget.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 自动调整列宽

        # 全局变量
        self.current_work_pth = os.getcwd()      #   要设置两个变量，一个是工作路径，一个是桌面上实训路径
        ## 桌面工作目录
        self.desktop_path = os.path.join(Path.home(),'Desktop','GZZC_LLM')

        self.model_pth = ''
        self.dataset_pth = ''
        self.model_testfile_pth = os.path.join(self.current_work_pth, 'external_files/chatglm3/utils.py')    #对于打包来说，这里肯定要改，1 相对路径 2 要在相应的文件夹下有文件
        self.model_utilfile_pth = os.path.join(self.current_work_pth, 'external_files/chatglm3/web.py')

        # data:数据集及配置文件放置位置  src:微调所需文件依赖
        self.data_folder = os.path.join(self.desktop_path,'data')
        self.src_folder = os.path.join(self.desktop_path,'src')
        # 创建文件夹路径
        if os.path.isdir(self.data_folder):
            pass
        else:
            os.mkdir(self.data_folder)
            print('data sucess')
        if os.path.isdir(self.src_folder):
            pass
        else:
            os.mkdir(self.src_folder)
            print('src sucess')

        #  列表显示图标设置
        py_pth = os.path.join(self.current_work_pth, 'external_files/images/python.png')            # 需要把一些外部引用的文件都放到一个文件夹内
        json_pth = os.path.join(self.current_work_pth, 'external_files/images/json.png')
        md_pth = os.path.join(self.current_work_pth, 'external_files/images/md.png')
        model_pth = os.path.join(self.current_work_pth, 'external_files/images/model.png')
        files_pth = os.path.join(self.current_work_pth, r'external_files/images/files.png')
        self.file_pth = os.path.join(self.current_work_pth, r'external_files/images/file.png')

        self.icon_mapping = {
            '.model': f'{files_pth}',
            '.md': f'{md_pth}',
            '.bin': f'{model_pth}',
            '.json': f'{json_pth}',
            '.py': f'{py_pth}',
            # 添加更多后缀名和对应的图标路径
        }
        self.font = QFont()
        self.font.setPointSize(10)

        #lineEdit
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)

        #PlainTextEdit
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_3.setReadOnly(True)

        self.bind()
    def bind(self):

        self.pushButton.clicked.connect(self.click)
        self.pushButton_7.clicked.connect(self.click3)
        self.pushButton_8.clicked.connect(self.click4)
        self.pushButton_3.clicked.connect(self.selectModeldir)
        self.pushButton_4.clicked.connect(self.selectDatasdir)
        self.pushButton_5.clicked.connect(self.exportDatasSetting)
        self.pushButton_12.clicked.connect(self.opencmd_window)
        self.pushButton_13.clicked.connect(self.redo)
        #   命令集
        self.pushButton_15.clicked.connect(self.orders)
        self.pushButton_14.clicked.connect(self.orders)
        self.pushButton_11.clicked.connect(self.orders)

        #   把该有的文件目录复制过去
        self.copy_folder_default()

        #在UI中定义了一个TreeWidegt ,给这个self.frame_3添加一个布局，把内容添加进去
        # self.tree_layout = QVBoxLayout(self.frame_3)
        # self.tree_layout.addWidget(self.treeWidget)




    def get_file_icon(self, file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension in self.icon_mapping:
            icon_path = self.icon_mapping[file_extension]
        else:
            icon_path = f'{self.file_pth}'  # 如果没有匹配的后缀名，则使用默认图标路径

        return QIcon(icon_path)

    def show_folder_contents(self, folder_path):
        self.treeWidget.clear()
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, filename)
            item.setIcon(0, self.get_file_icon(file_path))      # 扩展名匹配图标，返回图标路径
            file_extension = os.path.splitext(filename)[1]
            item.setText(1, file_extension)
            self.treeWidget.addTopLevelItem(item)


    def selectModeldir(self):   #  selectModeldir——>show_folder_contents——>get_file_icon
        self.model_pth = QFileDialog.getExistingDirectory(self, '请选择LLM模型所在文件夹')
        if self.model_pth:
            self.lineEdit.setText(self.model_pth)
            self.show_folder_contents(f'{self.model_pth}')
        else:
            QMessageBox.warning(self, '提示', '未选择文件夹')

    def selectDatasdir(self):   #   selectDatasdir——>show_datasets
        self.dataset_pth = QFileDialog.getOpenFileName(self, '请选择微调的数据集')[0]
        if self.dataset_pth:
            if not self.dataset_pth.endswith('.json'):
                QMessageBox.warning(self, '提示', '文本格式不正确')
                return

            # 检查文件内容是否为空
            if os.path.getsize(self.dataset_pth) == 0:
                QMessageBox.warning(self, '提示', '文件内容不存在')
                return

            self.lineEdit_2.setText(self.dataset_pth)
            self.show_datasets(self.dataset_pth)
            self.copy_file_dts()
        else:
            QMessageBox.warning(self, '提示', '选择数据集文件')

    def show_datasets(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        text = json.dumps(data, ensure_ascii=False, indent=4)
        self.textEdit.clear()
        
        # 设置关键字和符号的颜色
        keywords_color = QColor(255, 0, 0)  # 红色
        symbols_color = QColor(0, 0, 255)  # 蓝色

        # 遍历关键字列表，将关键字替换为带颜色的文本
        keywords = ['instruction', 'input', 'output']
        for keyword in keywords:
            # text = text.replace(f'"{keyword}"', f'<span style="color:{keywords_color.name()}">{keyword}</span>')
            text = text.replace(f'{keyword}', f'<span style="color:{keywords_color.name()}">{keyword}</span>')

        # 遍历符号列表，将符号替换为带颜色的文本
        symbols = ['{', '}', ',']
        for symbol in symbols:
            text = text.replace(symbol, f'<span style="color:{symbols_color.name()}">{symbol}</span>')

        # 设置富文本格式的文本到textEdit中
        self.textEdit.setHtml(f'<pre>{text}</pre>')

    def exportDatasSetting(self):
        if self.lineEdit.text() == '' or  self.lineEdit_2.text() == '' :
            QMessageBox.warning(self, '提示', '生成失败，请检查是否导入相关文件！')
        else:
            import hashlib
            import json
            #   获取数据集的哈希值
            with open(f'{self.dataset_pth}', 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(self.dataset_pth)
            json_str = json.dumps(data, sort_keys=True)
            sha1_hash = hashlib.sha1(json_str.encode()).hexdigest()
            name = os.path.splitext(os.path.basename(self.dataset_pth))[0]
            fullname = os.path.basename(self.dataset_pth)

            data = {
                "alpaca_zh": {
                    "file_name": "alpaca_data_zh_51k.json",
                    "file_sha1": "e655af3db557a4197f7b0cf92e1986b08fae6311"
                },
                name: {
                    "file_name": fullname,
                    "file_sha1": sha1_hash
                }
            }
            print(data)
            # 将数据写入 JSON 文件
            try:
                outfile_pth = os.path.join(self.desktop_path,'data','dataset_info.json')
                with open(f'{outfile_pth}', 'w') as f:
                    json.dump(data, f, indent=4)
                    f.flush()
                QMessageBox.information(self, '提示', '导出成功！', QMessageBox.StandardButton.Ok )
            except:
                QMessageBox.information(self, '提示', '导出失败！', QMessageBox.StandardButton.No)
    def orders(self):   #   页面3

        sender_button = self.sender()
        if sender_button == self.pushButton_11: #   训练
            self.train_data()
        elif sender_button == self.pushButton_14:   #   测试
            self.test_train_data()
        elif sender_button == self.pushButton_15:   #   导出
            self.export_trainresult()

    def train_data(self):

        dataset_name = os.path.splitext(os.path.basename(self.dataset_pth))[0]
        self.train_parameter_text = """import os
import subprocess

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

command = [
    'python',
    'src/train_bash.py',
    '--stage', 'sft',
    '--model_name_or_path', '{}',
    '--do_train',
    '--dataset', '{}',
    '--finetuning_type', 'lora',
    '--output_dir', 'checkpoint_output',
    '--per_device_train_batch_size', '2',
    '--gradient_accumulation_steps', '2',
    '--lr_scheduler_type', 'cosine',
    '--logging_steps', '10',
    '--save_steps', '1000',
    '--learning_rate', '5e-5',
    '--num_train_epochs', '20',
    '--plot_loss',
    '--fp16'
]

subprocess.call(command)
                """.format(self.model_pth,dataset_name)

        train_file = os.path.join(self.desktop_path,'train.py')
        with open(f'{train_file}', 'w',encoding='utf-8') as file:
            file.write(self.train_parameter_text)

        self.plainTextEdit_3.setPlainText(self.train_parameter_text)

    def test_train_data(self):

        checkpoint_pth = os.path.join(self.desktop_path,'checkpoint_output')
        self.test_parameter_text = """       
import subprocess
from src import  timer

command = [
    'python',
    'src/web_demo.py',
    '--model_name_or_path', '{}',
    '--finetuning_type', 'lora',
    '--checkpoint_dir', r'{}'
]

# 控制服务运行时常
timer.run_command_with_timeout(command, 60)
    """.format(self.model_pth,checkpoint_pth)

        test_file = os.path.join(self.desktop_path,'test.py')

        with open(f'{test_file}', 'w', encoding='utf-8') as file:
            file.write(self.test_parameter_text)

        self.plainTextEdit.setPlainText(self.test_parameter_text)


    def export_trainresult(self):

        checkpoint_pth = os.path.join(self.desktop_path, 'checkpoint_output')
        modelfiles = os.path.join(self.desktop_path,'model_output')
        #   写python执行文件
        self.export_parameter_text = '''import subprocess

command = [
    'python',
    'src/export_model.py',
    '--model_name_or_path',
    r'{}',
    '--finetuning_type',
    'lora',
    '--checkpoint_dir',
    r'{}',
    '--output_dir',
    r'{}'
]

subprocess.call(command)
        '''.format(self.model_pth,checkpoint_pth,modelfiles)        # 文件内容

        #   写入位置
        export_file = os.path.join(self.desktop_path,'export.py')

        with open(f'{export_file}', 'w', encoding='utf-8') as file:
            file.write(self.export_parameter_text)

        #   在软件中显示python文本
        self.plainTextEdit_2.setPlainText(self.export_parameter_text)
        self.copy_file_modeltest()

    def opencmd_window(self):
        # dir_path = os.path.abspath(os.path.dirname(__file__))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = os.path.join(dir_path, "programs\\cmd.bat")
        subprocess.call(['cmd', '/c', 'start', '', '/b', bat_path],creationflags=subprocess.CREATE_NEW_CONSOLE)

    def redo(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit.clear()
        self.treeWidget.clear()

    def copy_folder_default(self):      #   打包后,代码也要能够找到源文件的位置
        source_folder = os.path.join(self.current_work_pth,'external_files/chatglm3/src')    #待修改
        shutil.copytree(source_folder, self.src_folder, dirs_exist_ok=True)

    def copy_file_dts(self):
        import shutil
        try:
            shutil.copy(self.dataset_pth, self.data_folder)
            print("文件复制成功！")
        except :
            pass

    def copy_file_modeltest(self):
        import shutil
        try:
            shutil.copy(self.model_testfile_pth, self.desktop_path)
            shutil.copy(self.model_utilfile_pth, self.desktop_path)
            print("文件model！")
        except :
            pass


    def click(self):
        self.stackedWidget.setCurrentIndex(1)


    def click3(self):
        self.stackedWidget.setCurrentIndex(2)

    def click4(self):
        self.stackedWidget.setCurrentIndex(0)
        self.plainTextEdit.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_2.clear()

if __name__ == '__main__':

    app = QApplication([])
    window = ThirdMainWindow()
    window.show()
    app.exec()