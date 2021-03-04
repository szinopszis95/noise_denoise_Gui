from PySide2.QtWidgets import QVBoxLayout, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setParent(parent)
        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.figure.tight_layout()
        self.canvas.axes.axis('tight')
        self.canvas.axes.axis('off')
        self.canvas.figure.patch.set_visible(False)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)
