# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rkwork.ui'
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
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_r

class Ui_RKwork(object):
    def setupUi(self, RKwork):
        if not RKwork.objectName():
            RKwork.setObjectName(u"RKwork")
        RKwork.resize(1389, 880)
        self.verticalLayout_5 = QVBoxLayout(RKwork)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(RKwork)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"#frame{border-image: url(:/image/images/image/topbg.png);}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(-10, 10, 621, 82))
        self.label_2.setStyleSheet(u"image: url(:/image/images/image/logo_title.png);")
        self.label_2.setLineWidth(0)
        self.close_btn = QPushButton(self.frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(1340, 20, 40, 40))
        self.close_btn.setCursor(QCursor(Qt.ClosedHandCursor))
        self.close_btn.setStyleSheet(u"border-image: url(:/icon/images/icon/ico07.png);")

        self.verticalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(RKwork)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(180, 0))
        self.frame_4.setStyleSheet(u"#frame_4{border-image: url(:/image/images/image/leftt.png);}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 300))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 40, 0)
        self.homePag_btn = QPushButton(self.frame_6)
        self.homePag_btn.setObjectName(u"homePag_btn")
        self.homePag_btn.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QFont.PreferDefault)
        self.homePag_btn.setFont(font)
        self.homePag_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.homePag_btn.setLayoutDirection(Qt.LeftToRight)
        self.homePag_btn.setStyleSheet(u"#homePag_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#homePag_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/images/icon/ico01.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePag_btn.setIcon(icon)
        self.homePag_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.homePag_btn)

        self.envDpl_btn = QPushButton(self.frame_6)
        self.envDpl_btn.setObjectName(u"envDpl_btn")
        self.envDpl_btn.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.envDpl_btn.setFont(font1)
        self.envDpl_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.envDpl_btn.setStyleSheet(u"#envDpl_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#envDpl_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icon/ico02.png", QSize(), QIcon.Normal, QIcon.Off)
        self.envDpl_btn.setIcon(icon1)
        self.envDpl_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.envDpl_btn)

        self.dataGen_btn = QPushButton(self.frame_6)
        self.dataGen_btn.setObjectName(u"dataGen_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.dataGen_btn.sizePolicy().hasHeightForWidth())
        self.dataGen_btn.setSizePolicy(sizePolicy2)
        self.dataGen_btn.setMinimumSize(QSize(0, 50))
        self.dataGen_btn.setFont(font1)
        self.dataGen_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.dataGen_btn.setStyleSheet(u"#dataGen_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#dataGen_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icon/ico03.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dataGen_btn.setIcon(icon2)
        self.dataGen_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.dataGen_btn)

        self.modelFtn_btn = QPushButton(self.frame_6)
        self.modelFtn_btn.setObjectName(u"modelFtn_btn")
        self.modelFtn_btn.setMinimumSize(QSize(0, 50))
        self.modelFtn_btn.setFont(font1)
        self.modelFtn_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.modelFtn_btn.setStyleSheet(u"#modelFtn_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#modelFtn_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/icon/ico04.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modelFtn_btn.setIcon(icon3)
        self.modelFtn_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.modelFtn_btn)

        self.modelTra_btn = QPushButton(self.frame_6)
        self.modelTra_btn.setObjectName(u"modelTra_btn")
        self.modelTra_btn.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setKerning(True)
        self.modelTra_btn.setFont(font2)
        self.modelTra_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.modelTra_btn.setStyleSheet(u"#modelTra_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#modelTra_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/icon/ico05.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modelTra_btn.setIcon(icon4)
        self.modelTra_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.modelTra_btn)

        self.existSys_btn = QPushButton(self.frame_6)
        self.existSys_btn.setObjectName(u"existSys_btn")
        self.existSys_btn.setMinimumSize(QSize(0, 50))
        self.existSys_btn.setFont(font1)
        self.existSys_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.existSys_btn.setStyleSheet(u"#existSys_btn{\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"}\n"
"\n"
"#existSys_btn:pressed{\n"
"color:rgb(255,255,255);\n"
"padding-right:8px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/images/icon/ico07.png", QSize(), QIcon.Normal, QIcon.Off)
        self.existSys_btn.setIcon(icon5)
        self.existSys_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.existSys_btn)


        self.verticalLayout.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border-image: url(:/image/images/image/center_index.png);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(RKwork)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	\n"
"	border-image: url(:/image/images/image/bottombg.png);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.retranslateUi(RKwork)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(RKwork)
    # setupUi

    def retranslateUi(self, RKwork):
        RKwork.setWindowTitle(QCoreApplication.translate("RKwork", u"Form", None))
        self.label_2.setText("")
        self.close_btn.setText("")
        self.homePag_btn.setText(QCoreApplication.translate("RKwork", u"\u8f6f\u4ef6\u9996\u9875", None))
        self.envDpl_btn.setText(QCoreApplication.translate("RKwork", u"\u73af\u5883\u90e8\u7f72", None))
        self.dataGen_btn.setText(QCoreApplication.translate("RKwork", u"\u5236\u6570\u636e\u96c6", None))
        self.modelFtn_btn.setText(QCoreApplication.translate("RKwork", u"\u6a21\u578b\u5fae\u8c03", None))
        self.modelTra_btn.setText(QCoreApplication.translate("RKwork", u"\u6a21\u578b\u5b9e\u8bad", None))
        self.existSys_btn.setText(QCoreApplication.translate("RKwork", u"\u9000\u51fa\u7cfb\u7edf", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("RKwork", u"\u7248\u6743\u6240\u6709\uff1a\u5e7f\u4e1c\u4f17\u627f\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u6709\u9650\u516c\u53f8", None))
    # retranslateUi

