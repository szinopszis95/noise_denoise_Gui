# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_base_v4dRKXpm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QIcon, QPalette)
from PySide2.QtWidgets import *

from GUI.mplwidget import MplWidget

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 1000)
        MainWindow.setMinimumSize(QSize(640, 480))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "	color: #ffffff;\n"
                                 "	background-color: rgba(27, 29, 35, 160);\n"
                                 "	border: 1px solid rgb(40, 40, 40);\n"
                                 "	border-radius: 2px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName("frame_main")
        with open("./GUI/qss_files/pyside.qss", "r") as stylefile:
            self.frame_main.setStyleSheet(stylefile.read())
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
                                           "	background-image: url(GUI/icons/24x24/cil-menu.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "	border: none;\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {	\n"
                                           "	background-color: rgb(85, 170, 255);\n"
                                           "}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(GUI/icons/16x16/cil-terminal.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
                                               "")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        with open("./GUI/qss_files/pushbutton.qss", "r") as stylefile:
            self.btn_minimize.setStyleSheet(stylefile.read())
        icon = QIcon()
        icon.addFile("GUI/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        with open("./GUI/qss_files/pushbutton.qss", "r") as stylefile:
            self.btn_maximize_restore.setStyleSheet(stylefile.read())
        icon1 = QIcon()
        icon1.addFile("GUI/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        with open("./GUI/qss_files/pushbutton.qss", "r") as stylefile:
            self.btn_close.setStyleSheet(stylefile.read())
        icon2 = QIcon()
        icon2.addFile(u"GUI/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily("Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily("Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)

        self.verticalLayout_2.addWidget(self.frame_top_info)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName("label_6")
        font5 = QFont()
        font5.setFamily("Segoe UI")
        font5.setPointSize(40)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName("label")
        font6 = QFont()
        font6.setFamily("Segoe UI")
        font6.setPointSize(14)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName("label_7")
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(15)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName("page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName("frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName("labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet("")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)

        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName("frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font8 = QFont()
        font8.setFamily("Segoe UI")
        font8.setPointSize(9)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 5px;	\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "QPushButton:pressed {	\n"
                                      "	background-color: rgb(35, 40, 49);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}")
        icon3 = QIcon()
        icon3.addFile(u"GUI/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.verticalLayout_7.addWidget(self.frame_content_wid_1)

        self.verticalLayout_15.addWidget(self.frame_div_content_1)

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        with open("./GUI/qss_files/frame.qss", "r") as frame_whatever:
            self.frame_2.setStyleSheet(frame_whatever.read())
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        with open("./GUI/qss_files/frame.qss", "r") as scrollarea:
            self.verticalScrollBar.setStyleSheet(scrollarea.read())
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        with open("./GUI/qss_files/frame.qss", "r") as scrollarea:
            self.scrollArea.setStyleSheet(scrollarea.read())
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        with open("./GUI/qss_files/plaintextedit.qss", "r") as textedit:
            self.plainTextEdit.setStyleSheet(textedit.read())

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(font8)
        self.comboBox.setAutoFillBackground(False)
        with open("./GUI/qss_files/combobox.qss", "r") as combobox:
            self.comboBox.setStyleSheet(combobox.read())
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet("QScrollBar:horizontal {\n"
                                               "    border: none;\n"
                                               "    background: rgb(52, 59, 72);\n"
                                               "    height: 14px;\n"
                                               "    margin: 0px 21px 0 21px;\n"
                                               "	border-radius: 0px;\n"
                                               "}\n"
                                               "")

        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        # with open("./GUI/qss_files/commandlink.qss", "r") as commandlink:
        #     self.commandLinkButton.setStyleSheet(commandlink.read())
        icon4 = QIcon()
        icon4.addFile(u"GUI/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.verticalLayout_11.addLayout(self.gridLayout_2)

        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
        # endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
        # endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
        # endif
        self.tableWidget.setPalette(palette1)
        # with open("./GUI/qss_files/tablewidget.qss", "r") as table_style:
        #     self.tableWidget.setStyleSheet(table_style.read())
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)

        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        ###GEN_SINO_PAGE ###
        self.page_gen_sino = QWidget()
        self.page_gen_sino.setObjectName("page_gen_sino")
        self.verticalLayout_25 = QVBoxLayout(self.page_gen_sino)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_4 = QFrame(self.page_gen_sino)
        self.frame_4.setStyleSheet("border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_div_content_2 = QFrame(self.frame_4)
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.frame_div_content_2.setObjectName("frame_div_content_2")
        self.verticalLayout_13 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_title_wid_3 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_3.setObjectName("frame_title_wid_3")
        self.verticalLayout_14 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_3)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet("")
        self.labelBoxBlenderInstalation_2.setObjectName("labelBoxBlenderInstalation_2")
        self.verticalLayout_14.addWidget(self.labelBoxBlenderInstalation_2)
        self.verticalLayout_13.addWidget(self.frame_title_wid_3)
        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_2.setObjectName("frame_content_wid_2")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_3 = QPushButton(self.frame_content_wid_2)
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_4.setObjectName("labelVersion_4")
        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 2)
        self.horizontalLayout_13.addLayout(self.gridLayout_3)
        self.verticalLayout_13.addWidget(self.frame_content_wid_2)
        self.verticalLayout_16.addWidget(self.frame_div_content_2)
        self.verticalLayout_25.addWidget(self.frame_4)
        self.frame_5 = QFrame(self.page_gen_sino)
        self.frame_5.setStyleSheet("border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_div_content_3 = QFrame(self.frame_5)
        self.frame_div_content_3.setMinimumSize(QSize(0, 110))
        self.frame_div_content_3.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_3.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_3.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_3.setFrameShadow(QFrame.Raised)
        self.frame_div_content_3.setObjectName("frame_div_content_3")
        self.verticalLayout_12 = QVBoxLayout(self.frame_div_content_3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_title_wid_2 = QFrame(self.frame_div_content_3)
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_2.setObjectName("frame_title_wid_2")
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_2)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet("")
        self.labelBoxBlenderInstalation_3.setObjectName("labelBoxBlenderInstalation_3")
        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation_3)
        self.verticalLayout_12.addWidget(self.frame_title_wid_2)
        self.frame_content_wid_3 = QFrame(self.frame_div_content_3)
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_3.setObjectName("frame_content_wid_3")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_3 = QLineEdit(self.frame_content_wid_3)
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.pushButton_2 = QPushButton(self.frame_content_wid_3)
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.labelVersion_5 = QLabel(self.frame_content_wid_3)
        self.labelVersion_5.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_5.setObjectName("labelVersion_5")
        self.gridLayout_4.addWidget(self.labelVersion_5, 1, 0, 1, 2)
        self.horizontalLayout_14.addLayout(self.gridLayout_4)
        self.verticalLayout_12.addWidget(self.frame_content_wid_3)
        self.verticalLayout_17.addWidget(self.frame_div_content_3)
        self.verticalLayout_25.addWidget(self.frame_5)
        self.frame_6 = QFrame(self.page_gen_sino)
        self.frame_6.setStyleSheet("border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_div_content_4 = QFrame(self.frame_6)
        self.frame_div_content_4.setMinimumSize(QSize(0, 110))
        self.frame_div_content_4.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_4.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_4.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_4.setFrameShadow(QFrame.Raised)
        self.frame_div_content_4.setObjectName("frame_div_content_4")
        self.verticalLayout_20 = QVBoxLayout(self.frame_div_content_4)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_title_wid_4 = QFrame(self.frame_div_content_4)
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_4.setObjectName("frame_title_wid_4")
        self.verticalLayout_21 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.labelBoxBlenderInstalation_4 = QLabel(self.frame_title_wid_4)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet("")
        self.labelBoxBlenderInstalation_4.setObjectName("labelBoxBlenderInstalation_4")
        self.verticalLayout_21.addWidget(self.labelBoxBlenderInstalation_4)
        self.verticalLayout_20.addWidget(self.frame_title_wid_4)
        self.frame_content_wid_4 = QFrame(self.frame_div_content_4)
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_4.setObjectName("frame_content_wid_4")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_content_wid_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_4 = QLineEdit(self.frame_content_wid_4)
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.pushButton_4 = QPushButton(self.frame_content_wid_4)
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.labelVersion_6 = QLabel(self.frame_content_wid_4)
        self.labelVersion_6.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_6.setLineWidth(1)
        self.labelVersion_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_6.setObjectName("labelVersion_6")
        self.gridLayout_5.addWidget(self.labelVersion_6, 1, 0, 1, 2)
        self.horizontalLayout_15.addLayout(self.gridLayout_5)
        self.verticalLayout_20.addWidget(self.frame_content_wid_4)
        self.verticalLayout_19.addWidget(self.frame_div_content_4)
        self.verticalLayout_25.addWidget(self.frame_6)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.sinogram_button = QPushButton(self.page_gen_sino)
        self.sinogram_button.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.sinogram_button.setFont(font)
        self.sinogram_button.setStyleSheet("QPushButton {\n"
                                           "    border: 2px solid rgb(52, 59, 72);\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: rgb(52, 59, 72);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(57, 65, 80);\n"
                                           "    border: 2px solid rgb(61, 70, 86);\n"
                                           "}\n"
                                           "QPushButton:pressed {    \n"
                                           "    background-color: rgb(35, 40, 49);\n"
                                           "    border: 2px solid rgb(43, 50, 61);\n"
                                           "}")
        self.sinogram_button.setIcon(icon3)
        self.sinogram_button.setObjectName("sinogram_button")
        self.horizontalLayout_17.addWidget(self.sinogram_button)
        spacerItem = QSpacerItem(879, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_25.addLayout(self.horizontalLayout_17)
        self.frame_7 = QFrame(self.page_gen_sino)
        self.frame_7.setStyleSheet("border-radius: 5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_div_content_5 = QFrame(self.frame_7)
        self.frame_div_content_5.setMinimumSize(QSize(0, 110))
        self.frame_div_content_5.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_5.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_5.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_5.setFrameShadow(QFrame.Raised)
        self.frame_div_content_5.setObjectName("frame_div_content_5")
        self.verticalLayout_23 = QVBoxLayout(self.frame_div_content_5)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_title_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_5.setObjectName("frame_title_wid_5")
        self.verticalLayout_24 = QVBoxLayout(self.frame_title_wid_5)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.labelBoxBlenderInstalation_5 = QLabel(self.frame_title_wid_5)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet("")
        self.labelBoxBlenderInstalation_5.setObjectName("labelBoxBlenderInstalation_5")
        self.verticalLayout_24.addWidget(self.labelBoxBlenderInstalation_5)
        self.verticalLayout_23.addWidget(self.frame_title_wid_5)
        self.frame_content_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_content_wid_5.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_5.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_5.setObjectName("frame_content_wid_5")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_content_wid_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.progressBar = QProgressBar(self.frame_content_wid_5)
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "    text-align: center\n"
                                       "}\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(85, 170, 255);\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_6.addWidget(self.progressBar, 0, 0, 1, 1)
        self.horizontalLayout_16.addLayout(self.gridLayout_6)
        self.verticalLayout_23.addWidget(self.frame_content_wid_5)
        self.verticalLayout_22.addWidget(self.frame_div_content_5)
        self.verticalLayout_25.addWidget(self.frame_7)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page_gen_sino)

        ##END_GEN_SINO_PAGE###

        ##RECON_SINO_PAGE##

        self.page_gen_sino = QWidget()
        self.page_gen_sino.setObjectName("page_gen_sino")
        self.verticalLayout_25 = QVBoxLayout(self.page_gen_sino)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_4 = QFrame(self.page_gen_sino)
        self.frame_4.setStyleSheet("border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_div_content_2 = QFrame(self.frame_4)
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.frame_div_content_2.setObjectName("frame_div_content_2")
        self.verticalLayout_13 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_title_wid_3 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_3.setObjectName("frame_title_wid_3")
        self.verticalLayout_14 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_3)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet("")
        self.labelBoxBlenderInstalation_2.setObjectName("labelBoxBlenderInstalation_2")
        self.verticalLayout_14.addWidget(self.labelBoxBlenderInstalation_2)
        self.verticalLayout_13.addWidget(self.frame_title_wid_3)
        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_2.setObjectName("frame_content_wid_2")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.pushButton_3 = QPushButton(self.frame_content_wid_2)
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_4.setObjectName("labelVersion_4")
        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 2)
        self.horizontalLayout_13.addLayout(self.gridLayout_3)
        self.verticalLayout_13.addWidget(self.frame_content_wid_2)
        self.verticalLayout_16.addWidget(self.frame_div_content_2)
        self.verticalLayout_25.addWidget(self.frame_4)
        self.frame_5 = QFrame(self.page_gen_sino)
        self.frame_5.setStyleSheet("border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_div_content_3 = QFrame(self.frame_5)
        self.frame_div_content_3.setMinimumSize(QSize(0, 110))
        self.frame_div_content_3.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_3.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_3.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_3.setFrameShadow(QFrame.Raised)
        self.frame_div_content_3.setObjectName("frame_div_content_3")
        self.verticalLayout_12 = QVBoxLayout(self.frame_div_content_3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_title_wid_2 = QFrame(self.frame_div_content_3)
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_2.setObjectName("frame_title_wid_2")
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_2)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet("")
        self.labelBoxBlenderInstalation_3.setObjectName("labelBoxBlenderInstalation_3")
        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation_3)
        self.verticalLayout_12.addWidget(self.frame_title_wid_2)
        self.frame_content_wid_3 = QFrame(self.frame_div_content_3)
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_3.setObjectName("frame_content_wid_3")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_3 = QLineEdit(self.frame_content_wid_3)
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.pushButton_2 = QPushButton(self.frame_content_wid_3)
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.labelVersion_5 = QLabel(self.frame_content_wid_3)
        self.labelVersion_5.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_5.setObjectName("labelVersion_5")
        self.gridLayout_4.addWidget(self.labelVersion_5, 1, 0, 1, 2)
        self.horizontalLayout_14.addLayout(self.gridLayout_4)
        self.verticalLayout_12.addWidget(self.frame_content_wid_3)
        self.verticalLayout_17.addWidget(self.frame_div_content_3)
        self.verticalLayout_25.addWidget(self.frame_5)
        self.frame_6 = QFrame(self.page_gen_sino)
        self.frame_6.setStyleSheet("border-radius: 5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_div_content_4 = QFrame(self.frame_6)
        self.frame_div_content_4.setMinimumSize(QSize(0, 110))
        self.frame_div_content_4.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_4.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_4.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_4.setFrameShadow(QFrame.Raised)
        self.frame_div_content_4.setObjectName("frame_div_content_4")
        self.verticalLayout_20 = QVBoxLayout(self.frame_div_content_4)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_title_wid_4 = QFrame(self.frame_div_content_4)
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_4.setObjectName("frame_title_wid_4")
        self.verticalLayout_21 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.labelBoxBlenderInstalation_4 = QLabel(self.frame_title_wid_4)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet("")
        self.labelBoxBlenderInstalation_4.setObjectName("labelBoxBlenderInstalation_4")
        self.verticalLayout_21.addWidget(self.labelBoxBlenderInstalation_4)
        self.verticalLayout_20.addWidget(self.frame_title_wid_4)
        self.frame_content_wid_4 = QFrame(self.frame_div_content_4)
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_4.setObjectName("frame_content_wid_4")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_content_wid_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_4 = QLineEdit(self.frame_content_wid_4)
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.pushButton_4 = QPushButton(self.frame_content_wid_4)
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.labelVersion_6 = QLabel(self.frame_content_wid_4)
        self.labelVersion_6.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_6.setLineWidth(1)
        self.labelVersion_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_6.setObjectName("labelVersion_6")
        self.gridLayout_5.addWidget(self.labelVersion_6, 1, 0, 1, 2)
        self.horizontalLayout_15.addLayout(self.gridLayout_5)
        self.verticalLayout_20.addWidget(self.frame_content_wid_4)
        self.verticalLayout_19.addWidget(self.frame_div_content_4)
        self.verticalLayout_25.addWidget(self.frame_6)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.sinogram_button = QPushButton(self.page_gen_sino)
        self.sinogram_button.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.sinogram_button.setFont(font)
        self.sinogram_button.setStyleSheet("QPushButton {\n"
                                           "    border: 2px solid rgb(52, 59, 72);\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: rgb(52, 59, 72);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(57, 65, 80);\n"
                                           "    border: 2px solid rgb(61, 70, 86);\n"
                                           "}\n"
                                           "QPushButton:pressed {    \n"
                                           "    background-color: rgb(35, 40, 49);\n"
                                           "    border: 2px solid rgb(43, 50, 61);\n"
                                           "}")

        icon_sino = QIcon()
        icon_sino.addFile("GUI/icons/dna-structure", QSize(16, 16), QIcon.Normal, QIcon.Off)
        self.sinogram_button.setIcon(icon_sino)
        self.sinogram_button.setObjectName("sinogram_button")
        self.horizontalLayout_17.addWidget(self.sinogram_button)
        spacerItem = QSpacerItem(879, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_25.addLayout(self.horizontalLayout_17)
        self.frame_7 = QFrame(self.page_gen_sino)
        self.frame_7.setStyleSheet("border-radius: 5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_div_content_5 = QFrame(self.frame_7)
        self.frame_div_content_5.setMinimumSize(QSize(0, 110))
        self.frame_div_content_5.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_5.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_5.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_5.setFrameShadow(QFrame.Raised)
        self.frame_div_content_5.setObjectName("frame_div_content_5")
        self.verticalLayout_23 = QVBoxLayout(self.frame_div_content_5)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_title_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_5.setObjectName("frame_title_wid_5")
        self.verticalLayout_24 = QVBoxLayout(self.frame_title_wid_5)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.labelBoxBlenderInstalation_5 = QLabel(self.frame_title_wid_5)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet("")
        self.labelBoxBlenderInstalation_5.setObjectName("labelBoxBlenderInstalation_5")
        self.verticalLayout_24.addWidget(self.labelBoxBlenderInstalation_5)
        self.verticalLayout_23.addWidget(self.frame_title_wid_5)
        self.frame_content_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_content_wid_5.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_5.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_5.setObjectName("frame_content_wid_5")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_content_wid_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.progressBar = QProgressBar(self.frame_content_wid_5)
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "    text-align: center\n"
                                       "}\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(85, 170, 255);\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_6.addWidget(self.progressBar, 0, 0, 1, 1)
        self.horizontalLayout_16.addLayout(self.gridLayout_6)
        self.verticalLayout_23.addWidget(self.frame_content_wid_5)
        self.verticalLayout_22.addWidget(self.frame_div_content_5)
        self.verticalLayout_25.addWidget(self.frame_7)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page_gen_sino)

        ###END_GEN_SINO_PAGE###

        ###RECON_SINO###

        self.page_reconstruct_sino = QWidget()
        self.page_reconstruct_sino.setObjectName("page_reconstruct_sino")
        self.verticalLayout_39 = QVBoxLayout(self.page_reconstruct_sino)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_8 = QFrame(self.page_reconstruct_sino)
        self.frame_8.setStyleSheet("border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_26 = QVBoxLayout(self.frame_8)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame_div_content_6 = QFrame(self.frame_8)
        self.frame_div_content_6.setMinimumSize(QSize(0, 110))
        self.frame_div_content_6.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_6.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_6.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_6.setFrameShadow(QFrame.Raised)
        self.frame_div_content_6.setObjectName("frame_div_content_6")
        self.verticalLayout_27 = QVBoxLayout(self.frame_div_content_6)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_title_wid_6 = QFrame(self.frame_div_content_6)
        self.frame_title_wid_6.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_6.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_6.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_6.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_6.setObjectName("frame_title_wid_6")
        self.verticalLayout_28 = QVBoxLayout(self.frame_title_wid_6)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.labelBoxBlenderInstalation_6 = QLabel(self.frame_title_wid_6)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet("")
        self.labelBoxBlenderInstalation_6.setObjectName("labelBoxBlenderInstalation_6")
        self.verticalLayout_28.addWidget(self.labelBoxBlenderInstalation_6)
        self.verticalLayout_27.addWidget(self.frame_title_wid_6)
        self.frame_content_wid_6 = QFrame(self.frame_div_content_6)
        self.frame_content_wid_6.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_6.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_6.setObjectName("frame_content_wid_6")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_content_wid_6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_5 = QLineEdit(self.frame_content_wid_6)
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_7.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.pushButton_5 = QPushButton(self.frame_content_wid_6)
        self.pushButton_5.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.labelVersion_7 = QLabel(self.frame_content_wid_6)
        self.labelVersion_7.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_7.setLineWidth(1)
        self.labelVersion_7.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_7.setObjectName("labelVersion_7")
        self.gridLayout_7.addWidget(self.labelVersion_7, 1, 0, 1, 2)
        self.horizontalLayout_18.addLayout(self.gridLayout_7)
        self.verticalLayout_27.addWidget(self.frame_content_wid_6)
        self.verticalLayout_26.addWidget(self.frame_div_content_6)
        self.verticalLayout_39.addWidget(self.frame_8)
        self.frame_10 = QFrame(self.page_reconstruct_sino)
        self.frame_10.setStyleSheet("border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_33 = QVBoxLayout(self.frame_10)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_div_content_8 = QFrame(self.frame_10)
        self.frame_div_content_8.setMinimumSize(QSize(0, 110))
        self.frame_div_content_8.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_8.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_8.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_8.setFrameShadow(QFrame.Raised)
        self.frame_div_content_8.setObjectName("frame_div_content_8")
        self.verticalLayout_34 = QVBoxLayout(self.frame_div_content_8)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_title_wid_8 = QFrame(self.frame_div_content_8)
        self.frame_title_wid_8.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_8.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_8.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_8.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_8.setObjectName("frame_title_wid_8")
        self.verticalLayout_35 = QVBoxLayout(self.frame_title_wid_8)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.labelBoxBlenderInstalation_9 = QLabel(self.frame_title_wid_8)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_9.setFont(font)
        self.labelBoxBlenderInstalation_9.setStyleSheet("")
        self.labelBoxBlenderInstalation_9.setObjectName("labelBoxBlenderInstalation_9")
        self.verticalLayout_35.addWidget(self.labelBoxBlenderInstalation_9)
        self.verticalLayout_34.addWidget(self.frame_title_wid_8)
        self.frame_content_wid_8 = QFrame(self.frame_div_content_8)
        self.frame_content_wid_8.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_8.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_8.setObjectName("frame_content_wid_8")
        self.horizontalLayout_19 = QHBoxLayout(self.frame_content_wid_8)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEdit_6 = QLineEdit(self.frame_content_wid_8)
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                      "}")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_9.addWidget(self.lineEdit_6, 0, 0, 1, 1)
        self.pushButton_6 = QPushButton(self.frame_content_wid_8)
        self.pushButton_6.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_9.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.labelVersion_8 = QLabel(self.frame_content_wid_8)
        self.labelVersion_8.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_8.setObjectName("labelVersion_8")
        self.gridLayout_9.addWidget(self.labelVersion_8, 1, 0, 1, 2)
        self.horizontalLayout_19.addLayout(self.gridLayout_9)
        self.verticalLayout_34.addWidget(self.frame_content_wid_8)
        self.verticalLayout_33.addWidget(self.frame_div_content_8)
        self.verticalLayout_39.addWidget(self.frame_10)
        self.frame_9 = QFrame(self.page_reconstruct_sino)
        # self.frame_9.setStyleSheet("border-radius: 5px;")
        with open ("./GUI/qss_files/frame.qss", "r") as frame_style:
            self.frame_9.setStyleSheet(frame_style.read())
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_30 = QVBoxLayout(self.frame_9)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_div_content_7 = QFrame(self.frame_9)
        self.frame_div_content_7.setMinimumSize(QSize(0, 110))
        self.frame_div_content_7.setMaximumSize(QSize(16777215, 110))
        # self.frame_div_content_7.setStyleSheet("background-color: rgb(41, 45, 56);\n"
        #                                        "border-radius: 5px;\n"
        #                                        "")
        self.frame_div_content_7.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_7.setFrameShadow(QFrame.Raised)
        self.frame_div_content_7.setObjectName("frame_div_content_7")
        self.verticalLayout_31 = QVBoxLayout(self.frame_div_content_7)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_title_wid_7 = QFrame(self.frame_div_content_7)
        self.frame_title_wid_7.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_7.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_7.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_7.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_7.setObjectName("frame_title_wid_7")
        self.verticalLayout_32 = QVBoxLayout(self.frame_title_wid_7)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.labelBoxBlenderInstalation_8 = QLabel(self.frame_title_wid_7)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_8.setFont(font)
        self.labelBoxBlenderInstalation_8.setStyleSheet("")
        self.labelBoxBlenderInstalation_8.setObjectName("labelBoxBlenderInstalation_8")
        self.verticalLayout_32.addWidget(self.labelBoxBlenderInstalation_8)
        self.verticalLayout_31.addWidget(self.frame_title_wid_7)
        self.frame_content_wid_7 = QFrame(self.frame_div_content_7)
        self.frame_content_wid_7.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_7.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_7.setObjectName("frame_content_wid_7")
        self.gridLayout_8 = QGridLayout(self.frame_content_wid_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.comboBox_2 = QComboBox(self.frame_content_wid_7)
        self.comboBox_2.setMinimumSize(QSize(250, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("QComboBox{\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding: 5px;\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    color: rgb(85, 170, 255);    \n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 10px;\n"
                                      "    selection-background-color: rgb(39, 44, 54);\n"
                                      "}")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_2, 0, 0, 1, 1)
        self.checkBox_2 = QCheckBox(self.frame_content_wid_7)
        self.checkBox_2.setMinimumSize(QSize(100, 0))
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_8.addWidget(self.checkBox_2, 0, 1, 1, 1)
        spacerItem2 = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_31.addWidget(self.frame_content_wid_7)
        self.verticalLayout_30.addWidget(self.frame_div_content_7)
        self.verticalLayout_39.addWidget(self.frame_9)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.sinogram_button_2 = QPushButton(self.page_reconstruct_sino)
        self.sinogram_button_2.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.sinogram_button_2.setFont(font)
        self.sinogram_button_2.setStyleSheet("QPushButton {\n"
                                             "    border: 2px solid rgb(52, 59, 72);\n"
                                             "    border-radius: 5px;    \n"
                                             "    background-color: rgb(52, 59, 72);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: rgb(57, 65, 80);\n"
                                             "    border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {    \n"
                                             "    background-color: rgb(35, 40, 49);\n"
                                             "    border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon_sino_2 = QIcon()
        icon_sino_2.addFile("GUI/icons/hammer", QSize(16, 16), QIcon.Normal, QIcon.Off)
        self.sinogram_button_2.setIcon(icon_sino_2)
        self.sinogram_button_2.setObjectName("sinogram_button_2")
        self.horizontalLayout_21.addWidget(self.sinogram_button_2)
        spacerItem3 = QSpacerItem(879, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem3)
        self.verticalLayout_39.addLayout(self.horizontalLayout_21)
        self.frame_11 = QFrame(self.page_reconstruct_sino)
        self.frame_11.setStyleSheet("border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_36 = QVBoxLayout(self.frame_11)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_div_content_9 = QFrame(self.frame_11)
        self.frame_div_content_9.setMinimumSize(QSize(0, 110))
        self.frame_div_content_9.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_9.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                               "border-radius: 5px;\n"
                                               "")
        self.frame_div_content_9.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_9.setFrameShadow(QFrame.Raised)
        self.frame_div_content_9.setObjectName("frame_div_content_9")
        self.verticalLayout_37 = QVBoxLayout(self.frame_div_content_9)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.frame_title_wid_9 = QFrame(self.frame_div_content_9)
        self.frame_title_wid_9.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_9.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_9.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_9.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_9.setObjectName("frame_title_wid_9")
        self.verticalLayout_38 = QVBoxLayout(self.frame_title_wid_9)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.labelBoxBlenderInstalation_10 = QLabel(self.frame_title_wid_9)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_10.setFont(font)
        self.labelBoxBlenderInstalation_10.setStyleSheet("")
        self.labelBoxBlenderInstalation_10.setObjectName("labelBoxBlenderInstalation_10")
        self.verticalLayout_38.addWidget(self.labelBoxBlenderInstalation_10)
        self.verticalLayout_37.addWidget(self.frame_title_wid_9)
        self.frame_content_wid_9 = QFrame(self.frame_div_content_9)
        self.frame_content_wid_9.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_9.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_9.setObjectName("frame_content_wid_9")
        self.horizontalLayout_20 = QHBoxLayout(self.frame_content_wid_9)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.progressBar_3 = QProgressBar(self.frame_content_wid_9)
        self.progressBar_3.setStyleSheet("QProgressBar{\n"
                                         "    background-color: rgb(27, 29, 35);\n"
                                         "    border-radius: 5px;\n"
                                         "    border: 2px solid rgb(64, 71, 88);\n"
                                         "    text-align: center\n"
                                         "}\n"
                                         "QProgressBar::chunk {\n"
                                         "    background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_11.addWidget(self.progressBar_3, 0, 0, 1, 1)
        self.horizontalLayout_20.addLayout(self.gridLayout_11)
        self.verticalLayout_37.addWidget(self.frame_content_wid_9)
        self.verticalLayout_36.addWidget(self.frame_div_content_9)
        self.verticalLayout_39.addWidget(self.frame_11)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.page_reconstruct_sino)

        ###END_RECON_SINO

        ###TRAIN_NEURAL_NET_PAGE##

        self.page_train_neural_net = QWidget()
        self.page_train_neural_net.setObjectName("page_train_neural_net")
        self.verticalLayout_44 = QVBoxLayout(self.page_train_neural_net)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_17 = QFrame(self.page_train_neural_net)
        self.frame_17.setStyleSheet("border-radius: 5px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_55 = QVBoxLayout(self.frame_17)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.frame_div_content_15 = QFrame(self.frame_17)
        self.frame_div_content_15.setMinimumSize(QSize(0, 110))
        self.frame_div_content_15.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_15.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_15.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_15.setFrameShadow(QFrame.Raised)
        self.frame_div_content_15.setObjectName("frame_div_content_15")
        self.verticalLayout_56 = QVBoxLayout(self.frame_div_content_15)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.frame_title_wid_15 = QFrame(self.frame_div_content_15)
        self.frame_title_wid_15.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_15.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_15.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_15.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_15.setObjectName("frame_title_wid_15")
        self.verticalLayout_57 = QVBoxLayout(self.frame_title_wid_15)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.labelBoxBlenderInstalation_16 = QLabel(self.frame_title_wid_15)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_16.setFont(font)
        self.labelBoxBlenderInstalation_16.setStyleSheet("")
        self.labelBoxBlenderInstalation_16.setObjectName("labelBoxBlenderInstalation_16")
        self.verticalLayout_57.addWidget(self.labelBoxBlenderInstalation_16)
        self.verticalLayout_56.addWidget(self.frame_title_wid_15)
        self.frame_content_wid_15 = QFrame(self.frame_div_content_15)
        self.frame_content_wid_15.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_15.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_15.setObjectName("frame_content_wid_15")
        self.horizontalLayout_22 = QHBoxLayout(self.frame_content_wid_15)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.lineEdit_11 = QLineEdit(self.frame_content_wid_15)
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_16.addWidget(self.lineEdit_11, 0, 0, 1, 1)
        self.pushButton_11 = QPushButton(self.frame_content_wid_15)
        self.pushButton_11.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_16.addWidget(self.pushButton_11, 0, 1, 1, 1)
        self.labelVersion_14 = QLabel(self.frame_content_wid_15)
        self.labelVersion_14.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_14.setObjectName("labelVersion_14")
        self.gridLayout_16.addWidget(self.labelVersion_14, 1, 0, 1, 2)
        self.horizontalLayout_22.addLayout(self.gridLayout_16)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lineEdit_12 = QLineEdit(self.frame_content_wid_15)
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_12.setPlaceholderText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_12.addWidget(self.lineEdit_12, 0, 0, 1, 1)
        self.pushButton_12 = QPushButton(self.frame_content_wid_15)
        self.pushButton_12.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_12.addWidget(self.pushButton_12, 0, 1, 1, 1)
        self.labelVersion_15 = QLabel(self.frame_content_wid_15)
        self.labelVersion_15.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_15.setObjectName("labelVersion_15")
        self.gridLayout_12.addWidget(self.labelVersion_15, 1, 0, 1, 2)
        self.horizontalLayout_22.addLayout(self.gridLayout_12)
        self.verticalLayout_56.addWidget(self.frame_content_wid_15)
        self.verticalLayout_55.addWidget(self.frame_div_content_15)
        self.verticalLayout_44.addWidget(self.frame_17)
        self.frame_18 = QFrame(self.page_train_neural_net)
        self.frame_18.setStyleSheet("border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_58 = QVBoxLayout(self.frame_18)
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.frame_div_content_16 = QFrame(self.frame_18)
        self.frame_div_content_16.setMinimumSize(QSize(0, 110))
        self.frame_div_content_16.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_16.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_16.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_16.setFrameShadow(QFrame.Raised)
        self.frame_div_content_16.setObjectName("frame_div_content_16")
        self.verticalLayout_59 = QVBoxLayout(self.frame_div_content_16)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.frame_title_wid_16 = QFrame(self.frame_div_content_16)
        self.frame_title_wid_16.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_16.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_16.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_16.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_16.setObjectName("frame_title_wid_16")
        self.verticalLayout_60 = QVBoxLayout(self.frame_title_wid_16)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.labelBoxBlenderInstalation_17 = QLabel(self.frame_title_wid_16)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_17.setFont(font)
        self.labelBoxBlenderInstalation_17.setStyleSheet("")
        self.labelBoxBlenderInstalation_17.setObjectName("labelBoxBlenderInstalation_17")
        self.verticalLayout_60.addWidget(self.labelBoxBlenderInstalation_17)
        self.verticalLayout_59.addWidget(self.frame_title_wid_16)
        self.frame_content_wid_16 = QFrame(self.frame_div_content_16)
        self.frame_content_wid_16.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_16.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_16.setObjectName("frame_content_wid_16")
        self.horizontalLayout_23 = QHBoxLayout(self.frame_content_wid_16)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lineEdit_13 = QLineEdit(self.frame_content_wid_16)
        self.lineEdit_13.setMinimumSize(QSize(0, 30))
        self.lineEdit_13.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_17.addWidget(self.lineEdit_13, 0, 0, 1, 1)
        self.pushButton_13 = QPushButton(self.frame_content_wid_16)
        self.pushButton_13.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_17.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.labelVersion_16 = QLabel(self.frame_content_wid_16)
        self.labelVersion_16.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_16.setObjectName("labelVersion_16")
        self.gridLayout_17.addWidget(self.labelVersion_16, 1, 0, 1, 2)
        self.horizontalLayout_23.addLayout(self.gridLayout_17)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_14 = QLineEdit(self.frame_content_wid_16)
        self.lineEdit_14.setMinimumSize(QSize(0, 30))
        self.lineEdit_14.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_14.setPlaceholderText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_13.addWidget(self.lineEdit_14, 0, 0, 1, 1)
        self.pushButton_14 = QPushButton(self.frame_content_wid_16)
        self.pushButton_14.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_13.addWidget(self.pushButton_14, 0, 1, 1, 1)
        self.labelVersion_17 = QLabel(self.frame_content_wid_16)
        self.labelVersion_17.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_17.setObjectName("labelVersion_17")
        self.gridLayout_13.addWidget(self.labelVersion_17, 1, 0, 1, 2)
        self.horizontalLayout_23.addLayout(self.gridLayout_13)
        self.verticalLayout_59.addWidget(self.frame_content_wid_16)
        self.verticalLayout_58.addWidget(self.frame_div_content_16)
        self.verticalLayout_44.addWidget(self.frame_18)
        self.frame_16 = QFrame(self.page_train_neural_net)
        # self.frame_16.setStyleSheet("border-radius: 5px;")
        with open ("./GUI/qss_files/frame.qss", "r") as frame_style:
            self.frame_16.setStyleSheet(frame_style.read())
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_52 = QVBoxLayout(self.frame_16)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_div_content_14 = QFrame(self.frame_16)
        self.frame_div_content_14.setMinimumSize(QSize(0, 110))
        self.frame_div_content_14.setMaximumSize(QSize(16777215, 110))
        # self.frame_div_content_14.setStyleSheet("background-color: rgb(41, 45, 56);\n"
        #                                         "border-radius: 5px;\n"
        #                                         "")
        self.frame_div_content_14.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_14.setFrameShadow(QFrame.Raised)
        self.frame_div_content_14.setObjectName("frame_div_content_14")
        self.verticalLayout_53 = QVBoxLayout(self.frame_div_content_14)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.frame_title_wid_14 = QFrame(self.frame_div_content_14)
        self.frame_title_wid_14.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_14.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_14.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_14.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_14.setObjectName("frame_title_wid_14")
        self.verticalLayout_54 = QVBoxLayout(self.frame_title_wid_14)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.labelBoxBlenderInstalation_15 = QLabel(self.frame_title_wid_14)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_15.setFont(font)
        self.labelBoxBlenderInstalation_15.setStyleSheet("")
        self.labelBoxBlenderInstalation_15.setObjectName("labelBoxBlenderInstalation_15")
        self.verticalLayout_54.addWidget(self.labelBoxBlenderInstalation_15)
        self.verticalLayout_53.addWidget(self.frame_title_wid_14)
        self.frame_content_wid_14 = QFrame(self.frame_div_content_14)
        self.frame_content_wid_14.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_14.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_14.setObjectName("frame_content_wid_14")
        self.horizontalLayout_24 = QHBoxLayout(self.frame_content_wid_14)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.comboBox_3 = QComboBox(self.frame_content_wid_14)
        self.comboBox_3.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("QComboBox{\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding: 5px;\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    color: rgb(85, 170, 255);    \n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 10px;\n"
                                      "    selection-background-color: rgb(39, 44, 54);\n"
                                      "}")
        self.comboBox_3.setIconSize(QSize(16, 16))
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_18.addWidget(self.comboBox_3, 0, 0, 1, 1)
        self.labelVersion_13 = QLabel(self.frame_content_wid_14)
        self.labelVersion_13.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_13.setObjectName("labelVersion_13")
        self.gridLayout_18.addWidget(self.labelVersion_13, 1, 0, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_18)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.comboBox_4 = QComboBox(self.frame_content_wid_14)
        self.comboBox_4.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet("QComboBox{\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding: 5px;\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    color: rgb(85, 170, 255);    \n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 10px;\n"
                                      "    selection-background-color: rgb(39, 44, 54);\n"
                                      "}")
        self.comboBox_4.setIconSize(QSize(16, 16))
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_15.addWidget(self.comboBox_4, 0, 0, 1, 1)
        self.labelVersion_18 = QLabel(self.frame_content_wid_14)
        self.labelVersion_18.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_18.setObjectName("labelVersion_18")
        self.gridLayout_15.addWidget(self.labelVersion_18, 1, 0, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_15)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.lineEdit_15 = QLineEdit(self.frame_content_wid_14)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)
        self.lineEdit_15.setMinimumSize(QSize(120, 30))
        self.lineEdit_15.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_14.addWidget(self.lineEdit_15, 0, 0, 1, 1)
        self.pushButton_15 = QPushButton(self.frame_content_wid_14)
        self.pushButton_15.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_15.setText("")
        icon5 = QIcon()
        icon5.addFile("GUI/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_14.addWidget(self.pushButton_15, 0, 1, 1, 1)
        self.labelVersion_19 = QLabel(self.frame_content_wid_14)
        self.labelVersion_19.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_19.setLineWidth(1)
        self.labelVersion_19.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_19.setObjectName("labelVersion_19")
        self.gridLayout_14.addWidget(self.labelVersion_19, 1, 0, 1, 1)
        self.pushButton_16 = QPushButton(self.frame_content_wid_14)
        self.pushButton_16.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_16.setText("")
        icon6 = QIcon()
        icon6.addFile("GUI/icons/16x16/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon6)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_14.addWidget(self.pushButton_16, 1, 1, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_14)
        self.checkBox_3 = QCheckBox(self.frame_content_wid_14)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setMinimumSize(QSize(100, 0))
        self.checkBox_3.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_3.setAutoFillBackground(False)
        self.checkBox_3.setStyleSheet("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_24.addWidget(self.checkBox_3)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem5)
        self.verticalLayout_53.addWidget(self.frame_content_wid_14)
        self.verticalLayout_52.addWidget(self.frame_div_content_14)
        self.verticalLayout_44.addWidget(self.frame_16)
        self.frame_19 = QFrame(self.page_train_neural_net)
        self.frame_19.setStyleSheet("border-radius: 5px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_61 = QVBoxLayout(self.frame_19)
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.frame_div_content_17 = QFrame(self.frame_19)
        self.frame_div_content_17.setMinimumSize(QSize(0, 110))
        self.frame_div_content_17.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_17.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_17.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_17.setFrameShadow(QFrame.Raised)
        self.frame_div_content_17.setObjectName("frame_div_content_17")
        self.verticalLayout_62 = QVBoxLayout(self.frame_div_content_17)
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.frame_title_wid_17 = QFrame(self.frame_div_content_17)
        self.frame_title_wid_17.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_17.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_17.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_17.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_17.setObjectName("frame_title_wid_17")
        self.verticalLayout_63 = QVBoxLayout(self.frame_title_wid_17)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.labelBoxBlenderInstalation_18 = QLabel(self.frame_title_wid_17)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_18.setFont(font)
        self.labelBoxBlenderInstalation_18.setStyleSheet("")
        self.labelBoxBlenderInstalation_18.setObjectName("labelBoxBlenderInstalation_18")
        self.verticalLayout_63.addWidget(self.labelBoxBlenderInstalation_18)
        self.verticalLayout_62.addWidget(self.frame_title_wid_17)
        self.frame_content_wid_17 = QFrame(self.frame_div_content_17)
        self.frame_content_wid_17.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_17.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_17.setObjectName("frame_content_wid_17")
        self.gridLayout_20 = QGridLayout(self.frame_content_wid_17)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.lineEdit_18 = QLineEdit(self.frame_content_wid_17)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy)
        self.lineEdit_18.setMinimumSize(QSize(120, 30))
        self.lineEdit_18.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_29.addWidget(self.lineEdit_18, 0, 0, 1, 1)
        self.pushButton_21 = QPushButton(self.frame_content_wid_17)
        self.pushButton_21.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_29.addWidget(self.pushButton_21, 0, 1, 1, 1)
        self.labelVersion_26 = QLabel(self.frame_content_wid_17)
        self.labelVersion_26.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_26.setLineWidth(1)
        self.labelVersion_26.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_26.setObjectName("labelVersion_26")
        self.gridLayout_29.addWidget(self.labelVersion_26, 1, 0, 1, 1)
        self.pushButton_22 = QPushButton(self.frame_content_wid_17)
        self.pushButton_22.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon6)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_29.addWidget(self.pushButton_22, 1, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_29, 0, 0, 1, 1)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.lineEdit_17 = QLineEdit(self.frame_content_wid_17)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy)
        self.lineEdit_17.setMinimumSize(QSize(120, 30))
        self.lineEdit_17.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_23.addWidget(self.lineEdit_17, 0, 0, 1, 1)
        self.pushButton_19 = QPushButton(self.frame_content_wid_17)
        self.pushButton_19.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_23.addWidget(self.pushButton_19, 0, 1, 1, 1)
        self.labelVersion_25 = QLabel(self.frame_content_wid_17)
        self.labelVersion_25.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_25.setLineWidth(1)
        self.labelVersion_25.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_25.setObjectName("labelVersion_25")
        self.gridLayout_23.addWidget(self.labelVersion_25, 1, 0, 1, 1)
        self.pushButton_20 = QPushButton(self.frame_content_wid_17)
        self.pushButton_20.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon6)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_23.addWidget(self.pushButton_20, 1, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_23, 0, 1, 1, 1)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.pushButton_18 = QPushButton(self.frame_content_wid_17)
        self.pushButton_18.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon6)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_22.addWidget(self.pushButton_18, 1, 1, 1, 1)
        self.labelVersion_24 = QLabel(self.frame_content_wid_17)
        self.labelVersion_24.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_24.setLineWidth(1)
        self.labelVersion_24.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_24.setObjectName("labelVersion_24")
        self.gridLayout_22.addWidget(self.labelVersion_24, 1, 0, 1, 1)
        self.pushButton_17 = QPushButton(self.frame_content_wid_17)
        self.pushButton_17.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_22.addWidget(self.pushButton_17, 0, 1, 1, 1)
        self.lineEdit_16 = QLineEdit(self.frame_content_wid_17)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy)
        self.lineEdit_16.setMinimumSize(QSize(120, 30))
        self.lineEdit_16.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_22.addWidget(self.lineEdit_16, 0, 0, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_22, 0, 2, 1, 1)
        self.checkBox_4 = QCheckBox(self.frame_content_wid_17)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setMinimumSize(QSize(100, 0))
        self.checkBox_4.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_4.setAutoFillBackground(False)
        self.checkBox_4.setStyleSheet("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_20.addWidget(self.checkBox_4, 0, 3, 1, 1)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem6, 0, 4, 1, 1)
        self.verticalLayout_62.addWidget(self.frame_content_wid_17)
        self.verticalLayout_61.addWidget(self.frame_div_content_17)
        self.verticalLayout_44.addWidget(self.frame_19)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.sinogram_button_3 = QPushButton(self.page_train_neural_net)
        self.sinogram_button_3.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.sinogram_button_3.setFont(font)
        self.sinogram_button_3.setStyleSheet("QPushButton {\n"
                                             "    border: 2px solid rgb(52, 59, 72);\n"
                                             "    border-radius: 5px;    \n"
                                             "    background-color: rgb(52, 59, 72);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: rgb(57, 65, 80);\n"
                                             "    border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {    \n"
                                             "    background-color: rgb(35, 40, 49);\n"
                                             "    border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon_sino_3 = QIcon()
        icon_sino_3.addFile("GUI/icons/artificial-intelligence", QSize(16, 16), QIcon.Normal, QIcon.Off)
        self.sinogram_button_3.setIcon(icon_sino_3)
        self.sinogram_button_3.setObjectName("sinogram_button_3")
        self.horizontalLayout_27.addWidget(self.sinogram_button_3)
        spacerItem7 = QSpacerItem(879, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem7)
        self.verticalLayout_44.addLayout(self.horizontalLayout_27)
        self.frame_12 = QFrame(self.page_train_neural_net)
        self.frame_12.setStyleSheet("border-radius: 5px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_40 = QVBoxLayout(self.frame_12)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.frame_div_content_10 = QFrame(self.frame_12)
        self.frame_div_content_10.setMinimumSize(QSize(0, 110))
        self.frame_div_content_10.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_10.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_10.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_10.setFrameShadow(QFrame.Raised)
        self.frame_div_content_10.setObjectName("frame_div_content_10")
        self.verticalLayout_41 = QVBoxLayout(self.frame_div_content_10)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.frame_title_wid_10 = QFrame(self.frame_div_content_10)
        self.frame_title_wid_10.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_10.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_10.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_10.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_10.setObjectName("frame_title_wid_10")
        self.verticalLayout_42 = QVBoxLayout(self.frame_title_wid_10)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.labelBoxBlenderInstalation_11 = QLabel(self.frame_title_wid_10)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_11.setFont(font)
        self.labelBoxBlenderInstalation_11.setStyleSheet("")
        self.labelBoxBlenderInstalation_11.setObjectName("labelBoxBlenderInstalation_11")
        self.verticalLayout_42.addWidget(self.labelBoxBlenderInstalation_11)
        self.verticalLayout_41.addWidget(self.frame_title_wid_10)
        self.frame_content_wid_10 = QFrame(self.frame_div_content_10)
        self.frame_content_wid_10.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_10.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_10.setObjectName("frame_content_wid_10")
        self.horizontalLayout_26 = QHBoxLayout(self.frame_content_wid_10)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.progressBar_4 = QProgressBar(self.frame_content_wid_10)
        self.progressBar_4.setStyleSheet("QProgressBar{\n"
                                         "    background-color: rgb(27, 29, 35);\n"
                                         "    border-radius: 5px;\n"
                                         "    border: 2px solid rgb(64, 71, 88);\n"
                                         "    text-align: center\n"
                                         "}\n"
                                         "QProgressBar::chunk {\n"
                                         "    background-color: rgb(85, 170, 255);\n"
                                         "}")
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_19.addWidget(self.progressBar_4, 0, 0, 1, 1)
        self.horizontalLayout_26.addLayout(self.gridLayout_19)
        self.verticalLayout_41.addWidget(self.frame_content_wid_10)
        self.verticalLayout_40.addWidget(self.frame_div_content_10)
        self.verticalLayout_44.addWidget(self.frame_12)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem8 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.horizontalLayout_28.addItem(spacerItem8)
        self.label_2 = QLabel(self.page_train_neural_net)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(320, 240))
        self.label_2.setMaximumSize(QSize(320, 240))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_28.addWidget(self.label_2, alignment=Qt.AlignHCenter)
        spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.horizontalLayout_28.addItem(spacerItem9)
        self.verticalLayout_44.addLayout(self.horizontalLayout_28)
        spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout_44.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.page_train_neural_net)

        ###END_NEURAL_NET_PAGE

        ###PRED_NEURAL_NET_PAGE

        self.page_show_pred = QWidget()
        self.page_show_pred.setObjectName("page_show_pred")
        self.verticalLayout_48 = QVBoxLayout(self.page_show_pred)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_20 = QFrame(self.page_show_pred)
        self.frame_20.setStyleSheet("border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_64 = QVBoxLayout(self.frame_20)
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.frame_div_content_18 = QFrame(self.frame_20)
        self.frame_div_content_18.setMinimumSize(QSize(0, 110))
        self.frame_div_content_18.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_18.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_18.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_18.setFrameShadow(QFrame.Raised)
        self.frame_div_content_18.setObjectName("frame_div_content_18")
        self.verticalLayout_65 = QVBoxLayout(self.frame_div_content_18)
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.frame_title_wid_18 = QFrame(self.frame_div_content_18)
        self.frame_title_wid_18.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_18.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_18.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_18.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_18.setObjectName("frame_title_wid_18")
        self.verticalLayout_66 = QVBoxLayout(self.frame_title_wid_18)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.labelBoxBlenderInstalation_19 = QLabel(self.frame_title_wid_18)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_19.setFont(font)
        self.labelBoxBlenderInstalation_19.setStyleSheet("")
        self.labelBoxBlenderInstalation_19.setObjectName("labelBoxBlenderInstalation_19")
        self.verticalLayout_66.addWidget(self.labelBoxBlenderInstalation_19)
        self.verticalLayout_65.addWidget(self.frame_title_wid_18)
        self.frame_content_wid_18 = QFrame(self.frame_div_content_18)
        self.frame_content_wid_18.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_18.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_18.setObjectName("frame_content_wid_18")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_content_wid_18)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.lineEdit_20 = QLineEdit(self.frame_content_wid_18)
        self.lineEdit_20.setMinimumSize(QSize(0, 30))
        self.lineEdit_20.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_20.setPlaceholderText("")
        self.lineEdit_20.setText("C:/Users/Jana/PycharmProjects/denoising_v0.1/test_data/noisy")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_25.addWidget(self.lineEdit_20, 0, 0, 1, 1)
        self.pushButton_25 = QPushButton(self.frame_content_wid_18)
        self.pushButton_25.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_25.setIcon(icon3)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_25.addWidget(self.pushButton_25, 0, 1, 1, 1)
        self.labelVersion_20 = QLabel(self.frame_content_wid_18)
        self.labelVersion_20.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_20.setObjectName("labelVersion_20")
        self.gridLayout_25.addWidget(self.labelVersion_20, 1, 0, 1, 2)
        self.horizontalLayout_30.addLayout(self.gridLayout_25)
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.labelVersion_21 = QLabel(self.frame_content_wid_18)
        self.labelVersion_21.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.labelVersion_21.setObjectName("labelVersion_21")
        self.gridLayout_26.addWidget(self.labelVersion_21, 1, 0, 1, 2)
        self.lineEdit_21 = QLineEdit(self.frame_content_wid_18)
        self.lineEdit_21.setMinimumSize(QSize(0, 30))
        self.lineEdit_21.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.lineEdit_21.setPlaceholderText("")
        self.lineEdit_21.setText("C:/Users/Jana/PycharmProjects/denoising_v0.1/test_data/ground_truth")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_26.addWidget(self.lineEdit_21, 0, 0, 1, 1)
        self.pushButton_26 = QPushButton(self.frame_content_wid_18)
        self.pushButton_26.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.pushButton_26.setIcon(icon3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_26.addWidget(self.pushButton_26, 0, 1, 1, 1)
        self.horizontalLayout_30.addLayout(self.gridLayout_26)
        self.verticalLayout_65.addWidget(self.frame_content_wid_18)
        self.verticalLayout_64.addWidget(self.frame_div_content_18)
        self.verticalLayout_48.addWidget(self.frame_20)
        self.frame_14 = QFrame(self.page_show_pred)
        # self.frame_14.setStyleSheet("border-radius: 5px;")
        with open ("./GUI/qss_files/frame.qss", "r") as frame_style:
            self.frame_14.setStyleSheet(frame_style.read())
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_69 = QVBoxLayout(self.frame_14)
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.frame_div_content_13 = QFrame(self.frame_14)
        self.frame_div_content_13.setMinimumSize(QSize(0, 110))
        self.frame_div_content_13.setMaximumSize(QSize(16777215, 110))
        # self.frame_div_content_13.setStyleSheet("background-color: rgb(41, 45, 56);\n"
        #                                         "border-radius: 5px;\n"
        #                                         "")
        self.frame_div_content_13.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_13.setFrameShadow(QFrame.Raised)
        self.frame_div_content_13.setObjectName("frame_div_content_13")
        self.verticalLayout_70 = QVBoxLayout(self.frame_div_content_13)
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.frame_title_wid_19 = QFrame(self.frame_div_content_13)
        self.frame_title_wid_19.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_19.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_19.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_19.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_19.setObjectName("frame_title_wid_19")
        self.verticalLayout_71 = QVBoxLayout(self.frame_title_wid_19)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.labelBoxBlenderInstalation_20 = QLabel(self.frame_title_wid_19)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_20.setFont(font)
        self.labelBoxBlenderInstalation_20.setStyleSheet("")
        self.labelBoxBlenderInstalation_20.setObjectName("labelBoxBlenderInstalation_20")
        self.verticalLayout_71.addWidget(self.labelBoxBlenderInstalation_20)
        self.verticalLayout_70.addWidget(self.frame_title_wid_19)
        self.frame_content_wid_12 = QFrame(self.frame_div_content_13)
        self.frame_content_wid_12.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_12.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_12.setObjectName("frame_content_wid_12")
        self.horizontalLayout_25 = QHBoxLayout(self.frame_content_wid_12)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comboBox_5 = QComboBox(self.frame_content_wid_12)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet("QComboBox{\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding: 5px;\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    color: rgb(85, 170, 255);    \n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 10px;\n"
                                      "    selection-background-color: rgb(39, 44, 54);\n"
                                      "}")
        self.comboBox_5.setIconSize(QSize(16, 16))
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_5, 0, 0, 1, 1)
        self.comboBox_6 = QComboBox(self.frame_content_wid_12)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setAutoFillBackground(False)
        self.comboBox_6.setStyleSheet("QComboBox{\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 2px solid rgb(27, 29, 35);\n"
                                      "    padding: 5px;\n"
                                      "    padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "    border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    color: rgb(85, 170, 255);    \n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 10px;\n"
                                      "    selection-background-color: rgb(39, 44, 54);\n"
                                      "}")
        self.comboBox_6.setIconSize(QSize(16, 16))
        self.comboBox_6.setFrame(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.pushButton_27 = QPushButton(self.frame_content_wid_12)
        self.pushButton_27.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        icon_predict = QIcon()
        icon_predict.addFile("GUI/icons/crystal-ball", QSize(16, 16), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon_predict)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_10.addWidget(self.pushButton_27, 0, 2, 1, 1)
        self.pushButton_28 = QPushButton(self.frame_content_wid_12)
        self.pushButton_28.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        icon_batch = QIcon()
        icon_batch.addFile("GUI/icons/16x16/cil-arrow-right", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon_batch)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_10.addWidget(self.pushButton_28, 0, 3, 1, 1)
        spacerItem9 = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 0, 4, 1, 1)
        self.horizontalLayout_25.addLayout(self.gridLayout_10)
        self.verticalLayout_70.addWidget(self.frame_content_wid_12)
        self.verticalLayout_69.addWidget(self.frame_div_content_13)
        self.verticalLayout_48.addWidget(self.frame_14)
        self.frame_15 = QFrame(self.page_show_pred)
        self.frame_15.setStyleSheet("border-radius: 5px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_72 = QVBoxLayout(self.frame_15)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.frame_div_content_19 = QFrame(self.frame_15)
        self.frame_div_content_19.setMinimumSize(QSize(0, 330))
        self.frame_div_content_19.setMaximumSize(QSize(16777215, 576))
        self.frame_div_content_19.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                                "border-radius: 5px;\n"
                                                "")
        self.frame_div_content_19.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_19.setFrameShadow(QFrame.Raised)
        self.frame_div_content_19.setObjectName("frame_div_content_19")
        self.verticalLayout_73 = QVBoxLayout(self.frame_div_content_19)
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.frame_title_wid_20 = QFrame(self.frame_div_content_19)
        self.frame_title_wid_20.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_20.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_20.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_20.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_20.setObjectName("frame_title_wid_20")
        self.verticalLayout_74 = QVBoxLayout(self.frame_title_wid_20)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.labelBoxBlenderInstalation_21 = QLabel(self.frame_title_wid_20)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_21.setFont(font)
        self.labelBoxBlenderInstalation_21.setStyleSheet("")
        self.labelBoxBlenderInstalation_21.setObjectName("labelBoxBlenderInstalation_21")
        self.verticalLayout_74.addWidget(self.labelBoxBlenderInstalation_21)
        self.verticalLayout_73.addWidget(self.frame_title_wid_20)
        self.frame_content_wid_13 = QFrame(self.frame_div_content_19)
        self.frame_content_wid_13.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_13.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_13.setObjectName("frame_content_wid_13")
        self.verticalLayout_51 = QVBoxLayout(self.frame_content_wid_13)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_f = QHBoxLayout()
        self.horizontalLayout_f.setObjectName("horizontalLayout")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.labelVersion_29 = QLabel(self.frame_content_wid_13)
        self.labelVersion_29.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_29.setLineWidth(1)
        self.labelVersion_29.setAlignment(Qt.AlignCenter)
        self.labelVersion_29.setObjectName("labelVersion_29")
        self.verticalLayout_29.addWidget(self.labelVersion_29)
        self.widget = MplWidget(self.frame_content_wid_13)
        self.widget.setMinimumSize(QSize(256, 256))
        self.widget.setObjectName("widget")
        self.verticalLayout_29.addWidget(self.widget)
        self.horizontalLayout_f.addLayout(self.verticalLayout_29)
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.labelVersion_30 = QLabel(self.frame_content_wid_13)
        self.labelVersion_30.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_30.setLineWidth(1)
        self.labelVersion_30.setAlignment(Qt.AlignCenter)
        self.labelVersion_30.setObjectName("labelVersion_30")
        self.verticalLayout_43.addWidget(self.labelVersion_30)
        self.widget_2 = MplWidget(self.frame_content_wid_13)
        self.widget_2.setMinimumSize(QSize(256, 256))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_43.addWidget(self.widget_2)
        self.horizontalLayout_f.addLayout(self.verticalLayout_43)
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.labelVersion_31 = QLabel(self.frame_content_wid_13)
        self.labelVersion_31.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_31.setLineWidth(1)
        self.labelVersion_31.setAlignment(Qt.AlignCenter)
        self.labelVersion_31.setObjectName("labelVersion_31")
        self.verticalLayout_45.addWidget(self.labelVersion_31)
        self.widget_3 = MplWidget(self.frame_content_wid_13)
        self.widget_3.setMinimumSize(QSize(256, 256))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_45.addWidget(self.widget_3)
        self.horizontalLayout_f.addLayout(self.verticalLayout_45)
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.labelVersion_32 = QLabel(self.frame_content_wid_13)
        self.labelVersion_32.setStyleSheet("color: rgb(98, 103, 111);")
        self.labelVersion_32.setLineWidth(1)
        self.labelVersion_32.setAlignment(Qt.AlignCenter)
        self.labelVersion_32.setObjectName("labelVersion_32")
        self.verticalLayout_49.addWidget(self.labelVersion_32)
        self.widget_4 = MplWidget(self.frame_content_wid_13)
        self.widget_4.setMinimumSize(QSize(256, 256))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_49.addWidget(self.widget_4)
        self.horizontalLayout_f.addLayout(self.verticalLayout_49)
        self.verticalLayout_51.addLayout(self.horizontalLayout_f)
        self.verticalLayout_73.addWidget(self.frame_content_wid_13)
        self.verticalLayout_72.addWidget(self.frame_div_content_19)
        self.verticalLayout_48.addWidget(self.frame_15)
        self.horizontalScrollBar_3 = QScrollBar(self.page_show_pred)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_3.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_3.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_3.setStyleSheet("QScrollBar:horizontal {\n"
                                                 "    border: none;\n"
                                                 "    background: rgb(52, 59, 72);\n"
                                                 "    height: 14px;\n"
                                                 "    margin: 0px 21px 0 21px;\n"
                                                 "    border-radius: 0px;\n"
                                                 "}\n"
                                                 "")
        self.horizontalScrollBar_3.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar_3.setObjectName("horizontalScrollBar_3")
        self.verticalLayout_48.addWidget(self.horizontalScrollBar_3)
        spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_48.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.page_show_pred)

        ###END_PRED_NEURAL_NET_PAGE

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName("label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName("label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
                                           "	background-image: url(GUI/icons/16x16/cil-size-grip.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)

        self.verticalLayout_4.addWidget(self.frame_grip)

        self.horizontalLayout_2.addWidget(self.frame_content_right)

        self.verticalLayout.addWidget(self.frame_center)

        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", "AI - Denoising application", None))
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", "Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", "Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", "Close", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(
            QCoreApplication.translate("MainWindow", "C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", "| HOME", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "A simple AI-based denoising application", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "by Janos Sztancs", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", "BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", "Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Open Blender", None))
        self.labelVersion_3.setText(
            QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe",
                                       None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", "CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", "RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", "Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", "1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", "2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", "3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", "New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", "New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", "Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", "Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", "Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", "Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        _translate = QCoreApplication.translate
        self.labelBoxBlenderInstalation_2.setText(_translate("MainWindow", "FILE SELECTION"))
        self.pushButton_3.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_4.setText(
            _translate("MainWindow", "Select input files to construct sinogram from (DCM, NRRD, NPY)"))
        self.labelBoxBlenderInstalation_3.setText(_translate("MainWindow", "SINOGRAM OUTPUT PATH"))
        self.pushButton_2.setText(_translate("MainWindow", "Open directoy"))
        self.labelVersion_5.setText(_translate("MainWindow", "Select sinogram output folder"))
        self.labelBoxBlenderInstalation_4.setText(_translate("MainWindow", "GROUND TRUTH OUTPUT PATH"))
        self.pushButton_4.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_6.setText(_translate("MainWindow", "Select ground truth output folder"))
        self.sinogram_button.setText(_translate("MainWindow", "Start sinogram generation"))
        self.labelBoxBlenderInstalation_5.setText(_translate("MainWindow", "PROGRESS"))
        self.labelBoxBlenderInstalation_6.setText(_translate("MainWindow", "FILE SELECTION"))
        self.pushButton_5.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_7.setText(_translate("MainWindow", "Select slices to reconstruct (NRRD)"))
        self.labelBoxBlenderInstalation_9.setText(_translate("MainWindow", "RECONSTRUCTED FILES OUTPUT PATH"))
        self.pushButton_6.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_8.setText(_translate("MainWindow", "Select folder to place noisy slices in"))
        self.labelBoxBlenderInstalation_8.setText(_translate("MainWindow", "SELECT RECONSTRUCTION METHOD"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "FBP - Astra"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "FBP - ODL"))
        self.checkBox_2.setText(_translate("MainWindow", "Padding"))
        self.sinogram_button_2.setText(_translate("MainWindow", "Start CT reconstruction"))
        self.labelBoxBlenderInstalation_10.setText(_translate("MainWindow", "PROGRESS"))
        self.labelBoxBlenderInstalation_16.setText(_translate("MainWindow", "SELECT TRAINING DATA X/Y PATH"))
        self.pushButton_11.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_14.setText(_translate("MainWindow", "Select training data folder"))
        self.pushButton_12.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_15.setText(_translate("MainWindow", "Select training label folder"))
        self.labelBoxBlenderInstalation_17.setText(_translate("MainWindow", "SELECT VALIDATION DATA X/Y PATH"))
        self.pushButton_13.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_16.setText(_translate("MainWindow", "Select validation data folder"))
        self.pushButton_14.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_17.setText(_translate("MainWindow", "Select validation label folder"))
        self.labelBoxBlenderInstalation_15.setText(_translate("MainWindow", "TRAINING MODEL SETTINGS"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Autoencoder"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "U-Net"))
        self.labelVersion_13.setText(_translate("MainWindow", "Model to train"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Adam"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "SGD"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "MSE"))
        self.labelVersion_18.setText(_translate("MainWindow", "Optimizer"))
        self.lineEdit_15.setText(_translate("MainWindow", "1e-3"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "1e-3"))
        self.labelVersion_19.setText(_translate("MainWindow", "Learning rate"))
        self.checkBox_3.setText(_translate("MainWindow", "Save model"))
        self.labelBoxBlenderInstalation_18.setText(_translate("MainWindow", "TRAINING MODEL SETTINGS"))
        self.lineEdit_18.setText(_translate("MainWindow", "10"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "1e-3"))
        self.labelVersion_26.setText(_translate("MainWindow", "Number of epochs"))
        self.lineEdit_17.setText(_translate("MainWindow", "10"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "1e-3"))
        self.labelVersion_25.setText(_translate("MainWindow", "Steps per epoch"))
        self.labelVersion_24.setText(_translate("MainWindow", "Batch size"))
        self.lineEdit_16.setText(_translate("MainWindow", "4"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "4"))
        self.checkBox_4.setText(_translate("MainWindow", "Plot loss"))
        self.sinogram_button_3.setText(_translate("MainWindow", "Start training"))
        self.labelBoxBlenderInstalation_11.setText(_translate("MainWindow", "PROGRESS"))
        self.labelBoxBlenderInstalation_19.setText(_translate("MainWindow", "SELECT TEST DATA X/Y PATH"))
        self.pushButton_25.setText(_translate("MainWindow", "Open directory"))
        self.labelVersion_20.setText(_translate("MainWindow", "Select test data folder"))
        self.labelVersion_21.setText(_translate("MainWindow", "Select test label folder"))
        self.pushButton_26.setText(_translate("MainWindow", "Open directory"))
        self.labelBoxBlenderInstalation_20.setText(_translate("MainWindow", "SELECT TRAINED MODELS TO COMPARE"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Autoencoder"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "U-Net"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Autoencoder"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "U-Net"))
        self.pushButton_27.setText(_translate("MainWindow", "Show predictions"))
        self.pushButton_28.setText(_translate("MainWindow", "Next batch"))
        self.labelBoxBlenderInstalation_21.setText(_translate("MainWindow", "SHOW PREDICTION"))
        self.labelVersion_29.setText(_translate("MainWindow", "Ground Truth"))
        self.labelVersion_30.setText(_translate("MainWindow", "Noisy reconstruction"))
        self.labelVersion_31.setText(_translate("MainWindow", "Model 1 Prediction"))
        self.labelVersion_32.setText(_translate("MainWindow", "Model 2 Prediction"))

        self.label_credits.setText(
            QCoreApplication.translate("MainWindow", "by Janos Sztancs", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", "v0.1", None))
    # retranslateUi

class button_style():
    style_bt_standard = (
        """
        QPushButton {
            background-image: ICON_REPLACE;
            background-position: left center;
            background-repeat: no-repeat;
            border: none;
            border-left: 28px solid rgb(27, 29, 35);
            background-color: rgb(27, 29, 35);
            text-align: left;
            padding-left: 45px;
        }
        QPushButton[Active=true] {
            background-image: ICON_REPLACE;
            background-position: left center;
            background-repeat: no-repeat;
            border: none;
            border-left: 28px solid rgb(27, 29, 35);
            border-right: 5px solid rgb(44, 49, 60);
            background-color: rgb(27, 29, 35);
            text-align: left;
            padding-left: 45px;
        }
        QPushButton:hover {
            background-color: rgb(33, 37, 43);
            border-left: 28px solid rgb(33, 37, 43);
        }
        QPushButton:pressed {
            background-color: rgb(85, 170, 255);
            border-left: 28px solid rgb(85, 170, 255);
        }
        """
    )