import platform
import threading

from GUI.ui_functions import *
from GUI.ui_styles import Ui_MainWindow
from gen_recon_sino.gen_sino import SinogramGeneration
from gen_recon_sino.gen_sino_astra import SinogramGeneration2
from gen_recon_sino.recon_sino import ReconSino
from neural_net_training.compare_models import CompareModels
from neural_net_training.train_nn import TrainNetwork
from rand_functions.helper_functions import clear_temp


class MainWindow(QMainWindow):
    progressChanged = QtCore.Signal(int)
    progressChanged_2 = QtCore.Signal(int)
    progressChanged_3 = QtCore.Signal(int)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """SYSTEM"""
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        """REMOVE STANDARD TITLE BAR"""
        UIFunctions.remove_title_bar(True)

        """WINDOW TITLE"""
        self.setWindowTitle('AI - Denoising application')
        UIFunctions.label_title(self, 'AI - Denoising application')
        UIFunctions.label_desc(self, 'sinogram generation, reconstruction and denoising shenanigans')

        start_size = QSize(700, 1000)
        self.resize(start_size)
        self.setMinimumSize(start_size)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        """TOGGLE MENU SIZE"""
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggle_menu(self, 220, True))

        """ADD MENUS"""
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.add_new_menu(self, "Home Page", "btn_home", "url(GUI/icons/16x16/cil-home.png)", True)
        UIFunctions.add_new_menu(self, "Custom Widgets", "btn_widgets", "url(GUI/icons/16x16/cil-equalizer.png)", False)
        UIFunctions.add_new_menu(self, "Generate sinogram", "btn_sino", "url(GUI/icons/dna-helix-16)", True)
        UIFunctions.add_new_menu(self, "Reconstruct sinogram", "btn_rec", "url(GUI/icons/hammer-2-16)", True)
        UIFunctions.add_new_menu(self, "Train neural network", "btn_train", "url(GUI/icons/brain-3-16)", True)
        UIFunctions.add_new_menu(self, "View results", "btn_predict", "url(GUI/icons/analytics-16)", True)

        """START MENU SELECTION"""
        UIFunctions.select_standard_menu(self, "btn_home")

        """START PAGE"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        """MOVE WINDOW / MAXIMIZE / RESTORE"""

        def move_window(event):
            if UIFunctions.return_status(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = move_window

        """LOAD DEFINITIONS"""
        UIFunctions.uidefinitions(self)

        """WIDGETS FUNCTIONS/PARAMETERS"""

        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_3, _lineEdit=self.ui.lineEdit_2)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_2, _lineEdit=self.ui.lineEdit_3)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_4, _lineEdit=self.ui.lineEdit_4)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_5, _lineEdit=self.ui.lineEdit_5)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_6, _lineEdit=self.ui.lineEdit_6)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_11, _lineEdit=self.ui.lineEdit_11)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_12, _lineEdit=self.ui.lineEdit_12)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_13, _lineEdit=self.ui.lineEdit_13)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_14, _lineEdit=self.ui.lineEdit_14)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_25, _lineEdit=self.ui.lineEdit_20)
        UIFunctions.connect_button_line(self, _pushButton=self.ui.pushButton_26, _lineEdit=self.ui.lineEdit_21)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_15, self.ui.lineEdit_15, '*', 1e-1, 10)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_16, self.ui.lineEdit_15, '/', 1e-5, 10)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_21, self.ui.lineEdit_18, '+', 100, 1)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_22, self.ui.lineEdit_18, '-', 2, 1)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_19, self.ui.lineEdit_17, '+', 2500, 10)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_20, self.ui.lineEdit_17, '-', 10, 10)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_17, self.ui.lineEdit_16, '+', 100, 1)
        UIFunctions.change_line_edit_val(self, self.ui.pushButton_18, self.ui.lineEdit_16, '-', 2, 1)
        self.ui.sinogram_button.clicked.connect(self.start_task)
        self.ui.sinogram_button_2.clicked.connect(self.start_task_2)
        self.ui.sinogram_button_3.clicked.connect(self.start_training)
        self.progressChanged.connect(self._progressChanged)
        self.progressChanged_2.connect(self._progressChanged_2)
        self.progressChanged_3.connect(self._progressChanged_3)
        self.ui.pushButton_27.clicked.connect(self.predict)
        self.ui.pushButton_28.clicked.connect(self.next_batch)
        self.ui.horizontalScrollBar_3.valueChanged.connect(self.scroll_value)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.show()

    def next_batch(self):
        self.predict()

    def predict(self):
        global x_batch
        global y_batch
        global y1_hat
        global y2_hat
        x_batch, y_batch, y1_hat, y2_hat = CompareModels(self.ui.lineEdit_20.text(), self.ui.lineEdit_21.text(),
                                                         int(self.ui.lineEdit_16.text()),
                                                         self.ui.comboBox_5.currentIndex(),
                                                         self.ui.comboBox_6.currentIndex(),
                                                         self.ui.horizontalScrollBar_3, self.ui.widget,
                                                         self.ui.widget_2, self.ui.widget_3, self.ui.widget_4, None,
                                                         None, None, None).predict()

    def scroll_value(self):
        CompareModels(self.ui.lineEdit_20.text(), self.ui.lineEdit_21.text(), int(self.ui.lineEdit_16.text()),
                      self.ui.comboBox_5.currentIndex(), self.ui.comboBox_6.currentIndex(),
                      self.ui.horizontalScrollBar_3, self.ui.widget, self.ui.widget_2, self.ui.widget_3,
                      self.ui.widget_4, x_batch, y_batch, y1_hat, y2_hat).scroll_value()

    @QtCore.Slot()
    def start_training(self):
        t = threading.Thread(target=TrainNetwork(self.ui.lineEdit_11.text(), self.ui.lineEdit_12.text(), int(self.ui.lineEdit_16.text()),
                     self.ui.lineEdit_13.text(), self.ui.lineEdit_14.text(), self.ui.comboBox_3.currentIndex(),
                     int(self.ui.lineEdit_18.text()), self.progressChanged_3, self.ui.label_2,
                     float(self.ui.lineEdit_15.text()),
                     self.ui.comboBox_4.currentIndex(), int(self.ui.lineEdit_17.text())).training, daemon=True)
        t.start()

    def stop_task(self):
        SinogramGeneration.FLAG = True

    @QtCore.Slot()
    def start_task(self):
        SinogramGeneration.FLAG = False
        t = threading.Thread(target=SinogramGeneration(
            self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_2.text(),
            self.progressChanged).start_sinogram_generation,
                             daemon=True)
        t.start()

    @QtCore.Slot()
    def start_task_2(self):
        if self.ui.checkBox_2.isChecked():
            flag = True
        else:
            flag = False

        t = threading.Thread(target=ReconSino(
            self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text(), flag, self.progressChanged_2,
            self.ui.comboBox_2.currentIndex()).start_reconstruction, daemon=True)
        t.start()

    @QtCore.Slot(int)
    def _progressChanged(self, val):
        self.ui.progressBar.setValue(val)

    @QtCore.Slot(int)
    def _progressChanged_2(self, val):
        self.ui.progressBar_3.setValue(val)

    @QtCore.Slot(int)
    def _progressChanged_3(self, val):
        self.ui.progressBar_4.setValue(val)

    """DYNAMIC MENUS FUNCTIONS"""

    def button(self):
        """GET BT CLICKED"""
        btn_widget = self.sender()

        # PAGE HOME
        if btn_widget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.reset_style(self, "btn_home")
            UIFunctions.label_page(self, "Home")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # PAGE NEW USER
        if btn_widget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.reset_style(self, "btn_new_user")
            UIFunctions.label_page(self, "New User")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # PAGE WIDGETS
        if btn_widget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.reset_style(self, "btn_widgets")
            UIFunctions.label_page(self, "Custom Widgets")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # PAGE GEN SINO
        if btn_widget.objectName() == "btn_sino":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_gen_sino)
            UIFunctions.reset_style(self, "btn_sino")
            UIFunctions.label_page(self, "Generate Sinogram")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))
        # PAGE RECON SINO
        if btn_widget.objectName() == "btn_rec":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_reconstruct_sino)
            UIFunctions.reset_style(self, "btn_rec")
            UIFunctions.label_page(self, "Reconstruct Sinogram")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))
        # PAGE TRAIN NN
        if btn_widget.objectName() == "btn_train":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_train_neural_net)
            UIFunctions.reset_style(self, "btn_train")
            UIFunctions.label_page(self, "Train neural network model")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        if btn_widget.objectName() == "btn_predict":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_show_pred)
            UIFunctions.reset_style(self, "btn_predict")
            UIFunctions.label_page(self, "Display predictions")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

    def closeEvent(self, event):
        clear_temp()
