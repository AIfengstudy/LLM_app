# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datamake.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtWidgets import (QFrame, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                             QSizePolicy, QVBoxLayout)

from modules.DataMake import resources_rc
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1112, 727)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"#frame{border-image: url(:/pic/gzzca_2.jpg);}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 1, -1, -1)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u":/pic/gzzca_Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.pushButton_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.groupBox = QGroupBox(self.frame_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(750, 40))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"\n"
"            border-width: 0px;\n"
"            border-style: solid;\n"
"\n"
"        }")
        self.groupBox.setInputMethodHints(Qt.ImhNone)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 13)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(750, 40))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.lineEdit.setFont(font2)

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(750, 40))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(13)
        self.lineEdit_2.setFont(font3)

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border-width:0px;\n"
"	border-style:solid\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 40))
        self.pushButton_3.setMaximumSize(QSize(100, 30))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"	border:none;\n"
"	color:rgb(0,0,0);\n"
"	border:3px solid rgb(0,0,0);\n"
"\n"
"}\n"
"#pushButton_3:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(120, 40))
        self.pushButton_2.setMaximumSize(QSize(100, 30))
        font5 = QFont()
        font5.setFamilies([u"\u5b8b\u4f53"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	border:none;\n"
"	color:rgb(0,0,0);\n"
"	border:3px solid rgb(0,0,0);\n"
"	\n"
"}\n"
"#pushButton_2:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 40))
        self.pushButton.setMaximumSize(QSize(100, 30))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border:none;\n"
"	background-color:rgb(0,0,0);\n"
"	color:rgb(255,255,255);\n"
"	border:3px solid rgb(0,0,0);\n"
"\n"
"}\n"
"#pushButton:hover{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0, 0 ,0);\n"
"}\n"
"#pushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"#frame_2 {border-image: url(:/pic/gzzca_2.jpg);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 4, 20, 10)
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font6 = QFont()
        font6.setFamilies([u"Microsoft JhengHei Light"])
        font6.setPointSize(12)
        self.plainTextEdit.setFont(font6)
        self.plainTextEdit.setStyleSheet(u"")
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlaceholderText(u"\u6570\u636e\u96c6\u663e\u793a\u533a\u57df")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4f17\u627f\u5236\u4f5c\u6570\u636e\u96c6\u677f\u5757", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u95ee\u9898", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7b54\u6848", None))
        self.groupBox_2.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"  \u5220\u9664\u4e00\u6761\u6570\u636e\u96c6  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u4e00\u6761\u6570\u636e\u96c6", u"7"))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u6570\u636e\u96c6", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u"\u6570\u636e\u96c6\u663e\u793a\u533a\u57df\n"
"", None))
    # retranslateUi

