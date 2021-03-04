from PySide2 import QtCore, QtGui
import os
from PySide2.QtCore import (QPropertyAnimation, QSize, Qt)
from PySide2.QtGui import (QColor, QFont)
from PySide2.QtWidgets import *

from GUI.ui_styles import button_style

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
count = 1


class UIFunctions(QMainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u"GUI/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u"GUI/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    def return_status(self):
        return GLOBAL_STATE

    def set_status(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enable_max_size(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def toggle_menu(self, max_width, enable):
        if enable:
            """GET WIDTH"""
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 70

            """SET MAX WIDTH"""
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            """ANIMATION"""
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    """SET TITLE BAR"""

    def remove_title_bar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    """LABEL TITLE"""

    def label_title(self, text):
        self.ui.label_title_bar_top.setText(text)

    """LABEL DESCRIPTION"""

    def label_desc(self, text):
        self.ui.label_top_info_1.setText(text)

    """DYNAMIC MENUS"""

    def add_new_menu(self, name, obj_name, icon, is_top_menu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count), self)
        button.setObjectName(obj_name)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(button_style.style_bt_standard.replace('ICON_REPLACE', icon))

        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.button)

        if is_top_menu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    """SELECT"""

    def select_menu(getStyle):
        select = getStyle + "QPushButton { border-right: 7px solid rgb(44, 49, 60); }"
        return select

    """DESELECT"""

    def deselect_menu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    """START SELECTION"""

    def select_standard_menu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.select_menu(w.styleSheet()))

    """RESET SELECTION"""

    def reset_style(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselect_menu(w.styleSheet()))

    """CHANGE PAGE LABEL TEXT"""

    def label_page(self, text):
        new_text = '| ' + text.upper()
        self.ui.label_top_info_2.setText(new_text)

    def uidefinitions(self):
        def double_click_maximize_restore(event):
            """IF DOUBLE CLICK CHANGE STATUS"""
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        """STANDARD TITLE BAR"""
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = double_click_maximize_restore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        """DROP SHADOW"""
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        """RESIZE WINDOW"""
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        """MINIMIZE"""
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        """MAXIMIZE/RESTORE"""
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        """CLOSE APPLICATION"""
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def change_line_edit_val(self, _button, _line, operation, limit, step_size):

        def change_val():
            val = float(_line.text())
            if val == limit:
                return
            if operation == '+' or operation == '*':
                if val < limit:
                    if operation == '+':
                        new_val = int(val + step_size)
                    if operation == '*':
                        new_val = val * step_size
            if operation == '-' or operation == '/':
                if val > limit:
                    if operation == '-':
                        new_val = int(val - step_size)
                    if operation == '/':
                        new_val = val / step_size
            _line.setText(str(new_val))

        _button.clicked.connect(change_val)
        _button.setAutoRepeat(True)

    def connect_button_line(self, _pushButton, _lineEdit):

        def _dialog():
            filePath = QFileDialog.getExistingDirectory(options=QFileDialog.DontUseNativeDialog)
            dir_name = QtCore.QFileInfo(filePath).filePath()
            _lineEdit.setText(dir_name)

        _pushButton.clicked.connect(_dialog)
