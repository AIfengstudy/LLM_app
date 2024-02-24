import subprocess
import threading
import signal
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.Qsci import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import keyword
import os

from PyQt5.QtCore import QThread, pyqtSignal,Qt

class RunScriptThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, script_name):
        QThread.__init__(self)
        self.script_name = script_name
        self.process = None

    def run(self):
        self.process = subprocess.Popen(['python', self.script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        def reader(pipe, pipe_name):
            while True:
                line = pipe.readline()
                if line == '' and self.process.poll() is not None:
                    break
                if line:
                    print(f'{pipe_name}: {line.strip()}')
                    self.signal.emit(line.strip())

        threading.Thread(target=reader, args=[self.process.stdout, 'stdout']).start()
        threading.Thread(target=reader, args=[self.process.stderr, 'stderr']).start()

        self.process.wait()

    def stop(self):
        if self.process:
            os.kill(self.process.pid, signal.SIGTERM)

class MyTextEdit(QTextEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()

class Highlight(QsciLexerPython):
    def __init__(self, parent):
        global Filename
        QsciLexerPython.__init__(self, parent)


        print(os.getcwd())
        font = QFont()
        font.setFamily('Courier')
        font.setPointSize(14)
        font.setFixedPitch(True)

        self.setFont(font)
        self.setColor(QColor(0, 0, 0))
        self.setPaper(QColor(255, 255, 255))

        self.setColor(QColor("#00FF00"), QsciLexerPython.ClassName)
        self.setColor(QColor("#B0171F"), QsciLexerPython.Keyword)
        self.setColor(QColor("#00FF00"), QsciLexerPython.Comment)
        self.setColor(QColor("#FF00FF"), QsciLexerPython.Number)
        self.setColor(QColor("#0000FF"), QsciLexerPython.DoubleQuotedString)
        self.setColor(QColor("#0000FF"), QsciLexerPython.SingleQuotedString)
        self.setColor(QColor("#288B22"), QsciLexerPython.TripleSingleQuotedString)
        self.setColor(QColor("#288B22"), QsciLexerPython.TripleDoubleQuotedString)
        self.setColor(QColor("#0000FF"), QsciLexerPython.FunctionMethodName)
        self.setColor(QColor("#191970"), QsciLexerPython.Operator)
        self.setColor(QColor("#000000"), QsciLexerPython.Identifier)
        self.setColor(QColor("#00FF00"), QsciLexerPython.CommentBlock)
        self.setColor(QColor("#0000FF"), QsciLexerPython.UnclosedString)
        self.setColor(QColor("#FFFF00"), QsciLexerPython.HighlightedIdentifier)
        self.setColor(QColor("#FF8000"), QsciLexerPython.Decorator)

        self.setFont(QFont('Courier', 12, weight=QFont.Bold), 5)
        self.setFont(QFont('Courier', 12, italic=True), QsciLexerPython.Comment)

class ForthMainWindow(QMainWindow):
    def __init__(self, parent=None, title='未命名', filenamearg=None):
        super(ForthMainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle(title)
        self.menuBar().setFont(QFont("微软雅黑", 14))

        font = QFont()
        font.setFamily('Courier')
        font.setPointSize(12)        #编辑器内字体大小
        font.setFixedPitch(True)


        self.setFont(font)
        self.editor = QsciScintilla()
        self.editor.setFont(font)

        # self.setCentralWidget(self.editor)
        # 给中央布局一个布局xsl
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QVBoxLayout()
        centralWidget.setLayout(self.layout)
        # self.push = QPushButton('我是一个按钮')
        # self.push = QPushButton('我是一个按钮')

        self.textEdit = MyTextEdit(self)
        self.textEdit.clicked.connect(self.display_frame)


        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.textEdit)

       # 初始状态隐藏
        self.textEdit.close()
        self.textEdit.setReadOnly(True)
        self.textEdit.setCursor(Qt.ArrowCursor)

        #编辑器的编码格式
        self.editor.setUtf8(True)
        self.editor.setMarginsFont(font)
        self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)
        # self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)
        self.editor.setMarginLineNumbers(0, True)

        self.editor.setEdgeMode(QsciScintilla.EdgeLine)
        self.editor.setEdgeColumn(80)
        self.editor.setEdgeColor(QColor(0, 0, 0))

        self.editor.setBraceMatching(QsciScintilla.StrictBraceMatch)

        self.editor.setIndentationsUseTabs(True)
        self.editor.setIndentationWidth(4)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)
        self.editor.setBackspaceUnindents(True)
        self.editor.setTabWidth(4)

        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor('#FFFFCD'))

        self.editor.setIndentationGuides(True)

        self.editor.setFolding(QsciScintilla.PlainFoldStyle)
        self.editor.setMarginWidth(2, 12)

        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
        self.editor.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)

        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.editor.setMarkerBackgroundColor(QColor("#FFFFFF"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.editor.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.editor.setAutoCompletionCaseSensitivity(True)
        self.editor.setAutoCompletionReplaceWord(False)
        self.editor.setAutoCompletionThreshold(1)
        self.editor.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
        self.lexer = Highlight(self.editor)
        self.editor.setLexer(self.lexer)
        self.mod = False
        self.__api = QsciAPIs(self.lexer)
        autocompletions = keyword.kwlist + ["abs", "all", "any", "basestring", "bool",
                                            "callable", "chr", "classmethod", "cmp", "compile",
                                            "complex", "delattr", "dict", "dir", "divmod",
                                            "enumerate", "eval", "execfile", "exit", "file",
                                            "filter", "float", "frozenset", "getattr", "globals",
                                            "hasattr", "hex", "id", "int", "isinstance",
                                            "issubclass", "iter", "len", "list", "locals", "map",
                                            "max", "min", "object", "oct", "open", "ord", "pow",
                                            "property", "range", "reduce", "repr", "reversed",
                                            "round", "set", "setattr", "slice", "sorted",
                                            "staticmethod", "str", "sum", "super", "tuple", "type",
                                            "vars", "zip", 'print']
        for ac in autocompletions:
            self.__api.add(ac)
        self.__api.prepare()
        self.editor.autoCompleteFromAll()
        if filenamearg:
            obj = open(filenamearg, 'r+', encoding='utf-8')
            try:
                self.editor.setText(obj.read())
            except:
                QMessageBox.warning(self, '警告', '无法打开此文件！', QMessageBox.Ok)
                self.editor.document().clear()
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        fileNewAction = self.createAction("新建", self.newfile,
                                          'Ctrl+N', "filenew", "创建Python文件")
        fileOpenAction = self.createAction("打开", self.fileopen,
                                           'Ctrl+O', "fileopen",
                                           "打开Python文件")
        self.fileSaveAction = self.createAction("保存", self.save,
                                                'Ctrl+S', "filesave", "保存Python文件")
        self.fileSaveAsAction = self.createAction("另存为",
                                                  self.saveas, None,
                                                  "用新名字保存文件")
        fileQuitAction = self.createAction("退出", self.close,
                                           "Ctrl+Q", "filequit", "退出")
        self.editCopyAction = self.createAction("撤销",
                                                self.editor.undo, 'Ctrl+Z', "editcopy",
                                                "撤销")
        self.editCutAction = self.createAction("重做", self.editor.redo,
                                               'Ctrl+Alt+Z', "editcut",
                                               "重做")
        self.findAction = self.createAction("查找",
                                            self.findtext, 'Ctrl+F', "editcopy",
                                            "查找")
        self.replaceAction = self.createAction("替换", None,
                                               'Ctrl+R', "editcut",
                                               "替换")
        self.runAction = self.createAction('运行', self.run, 'Ctrl+B', '', '运行程序')


        self.stopAction = self.createAction('终止',self.stop, 'Ctrl+X','','终止程序')

        fileMenu = self.menuBar().addMenu("文件")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,
                                   self.fileSaveAction, self.fileSaveAsAction, None,
                                   fileQuitAction))
        editMenu = self.menuBar().addMenu("编辑")
        self.addActions(editMenu, (self.editCopyAction,
                                   self.editCutAction, None, self.findAction, self.replaceAction))
        runMenu = self.menuBar().addMenu('运行')
        self.addActions(runMenu, (self.runAction,self.stopAction))
        self.name = ''
        self.editor.textChanged.connect(self.changed)
        self.filename = filenamearg



    def run(self):
        self.textEdit.clear()

        global Filename
        script_name =Filename

        self.run_script_thread = RunScriptThread(script_name)
        self.run_script_thread.signal.connect(self.update_output)
        self.run_script_thread.start()

    def stop(self):
        if self.run_script_thread is not None and self.run_script_thread.isRunning():
            self.run_script_thread.stop()

    def update_output(self, text):
        self.textEdit.show()
        text = text.decode('utf-8')
        self.textEdit.append(text)

    def display_frame(self):
        self.textEdit.close()
        # print('TextEdit点击')
    def changed(self):
        self.mod = True
        self.editor.setMarginWidth(0, len(str(len(self.editor.text().split('\n')))) * 20)

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def askforsave(self):
        if self.mod:
            r = QMessageBox.question(self, '询问', '是否要保存?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if r == QMessageBox.Cancel:
                return False
            elif r == QMessageBox.Yes:
                return self.save()
            return True

    def save(self):
        if not self.name:
            return self.saveas()
        self.mod = False
        self.setWindowTitle(self.name)
        obj = open(self.name, 'w', encoding='utf-8')
        obj.truncate()
        obj.close()
        obj = open(self.name, 'r+', encoding='utf-8')
        try:
            obj.write(self.editor.text())
        except:
            obj.write('An error has occcured when trying to save this file.')
        obj.close()

    def saveas(self):
        filename, _buff = QFileDialog.getSaveFileName(self, '另存为', './', 'Python文件 (*.py)')
        if filename:
            self.name = filename
            return self.save()
        return False

    def newfile(self):
        if self.mod:
            if not self.askforsave():
                return -1
        self.editor.clear()
        self.mod = False
        self.name = ''
        self.setWindowTitle('未命名')

    def fileopen(self):
        os.chdir(r'C:\Users\rkwork\Desktop\GZZC_LLM')
        global Filename
        if self.mod:
            if not self.askforsave():
                return -1
        filename, _buff = QFileDialog.getOpenFileName(self, '打开', './', 'Python文件 (*.py)')
        Filename = filename
        print(Filename)

        if filename:
            self.name = filename
            obj = open(self.name, 'r+', encoding='utf-8')
            try:
                self.editor.setText(obj.read())
            except Exception as e:
                obj.close()
                self.setWindowTitle(self.name)
                self.mod = False

        def closeEvent(self, event):
            if not self.askforsave():
                event.ignore()
            event.accept()
            self.editor.setText("Can't read this file!Error:" + str(e))

    def findtext(self):
        pass


def main():
    import sys
    from os import path
    app = QApplication(sys.argv)
    fname = '未命名'
    if len(sys.argv) > 1:
        if path.isfile(sys.argv[1]):
            fname = sys.argv[1]
    form = ForthMainWindow(None, fname, fname if fname != '未命名' else None)
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()