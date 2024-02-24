# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'envBuild.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1012, 703)
        self.next_page_btn = QPushButton(Form)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setGeometry(QRect(9, 545, 100, 25))
        self.next_page_btn.setMinimumSize(QSize(100, 25))
        self.next_page_btn.setMaximumSize(QSize(100, 25))
        font = QFont()
        font.setPointSize(12)
        self.next_page_btn.setFont(font)
        self.next_page_btn.setStyleSheet(u"")
        self.opencmd_btn = QPushButton(Form)
        self.opencmd_btn.setObjectName(u"opencmd_btn")
        self.opencmd_btn.setGeometry(QRect(9, 576, 100, 25))
        self.opencmd_btn.setMinimumSize(QSize(100, 25))
        self.opencmd_btn.setMaximumSize(QSize(100, 25))
        self.opencmd_btn.setFont(font)
        self.opencmd_btn.setStyleSheet(u"")
        self.previous_page_btn = QPushButton(Form)
        self.previous_page_btn.setObjectName(u"previous_page_btn")
        self.previous_page_btn.setGeometry(QRect(9, 607, 100, 25))
        self.previous_page_btn.setMinimumSize(QSize(100, 25))
        self.previous_page_btn.setMaximumSize(QSize(25, 16777215))
        self.previous_page_btn.setFont(font)
        self.previous_page_btn.setStyleSheet(u"")
        self.home_page_btn = QPushButton(Form)
        self.home_page_btn.setObjectName(u"home_page_btn")
        self.home_page_btn.setGeometry(QRect(9, 638, 100, 25))
        self.home_page_btn.setMinimumSize(QSize(100, 25))
        self.home_page_btn.setMaximumSize(QSize(100, 25))
        self.home_page_btn.setFont(font)
        self.home_page_btn.setStyleSheet(u"")
        self.back_page_btn = QPushButton(Form)
        self.back_page_btn.setObjectName(u"back_page_btn")
        self.back_page_btn.setGeometry(QRect(9, 669, 100, 25))
        self.back_page_btn.setMinimumSize(QSize(100, 25))
        self.back_page_btn.setMaximumSize(QSize(100, 25))
        self.back_page_btn.setFont(font)
        self.back_page_btn.setStyleSheet(u"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 53, 16))
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.next_page_btn.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9875", None))
        self.opencmd_btn.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u642d\u5efa", None))
        self.previous_page_btn.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9875", None))
        self.home_page_btn.setText(QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.back_page_btn.setText(QCoreApplication.translate("Form", u"\u5c3e\u9875", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

