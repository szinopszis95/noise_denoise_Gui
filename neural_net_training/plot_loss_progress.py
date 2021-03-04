import matplotlib.pyplot as plt
from PySide2 import QtCore
from PySide2.QtGui import QPixmap
from tensorflow.keras.callbacks import Callback

from rand_functions.helper_functions import rescale


class PlotLosses(Callback):
    def __init__(self, num_epochs, progressbar, label):
        Callback.__init__(self)
        self.num_epochs = num_epochs
        self.progressbar = progressbar
        self.label = label
        self.progress = None
        self.increment = None
        self.i = None
        self.x = None
        self.losses = None
        self.val_losses = None
        self.logs = None

    def on_train_begin(self, num_epochs, logs={}):
        self.progress = 0
        self.increment = rescale(1, self.num_epochs)
        self.i = 1
        self.x = []
        self.losses = []
        self.val_losses = []
        self.logs = []
        plt.figure()
        plt.xlim(1, self.num_epochs)
        plt.ylim(0, 1)
        plt.plot(0, 0, label="loss")
        plt.plot(0, 0, label="val_loss")
        plt.title("Training and Validation loss [Epoch {}]".format(0))
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.savefig('temp/Epoch-{}.png'.format(0))
        pixmap = QPixmap('temp/Epoch-{}.png'.format(0))
        scaled_pixmap = pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(scaled_pixmap)
        plt.close()

    def on_epoch_end(self, epoch, logs={}):
        self.progress += self.increment
        self.progressbar.emit(self.progress)

        self.x.append(self.i)
        self.logs.append(logs)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.i += 1

        if len(self.losses) > 1:
            plt.figure()
            plt.xlim(1, self.num_epochs)
            plt.ylim(0, 1)
            plt.plot(self.x, self.losses, label="loss")
            plt.plot(self.x, self.val_losses, label="val_loss")
            plt.title("Training and Validation loss [Epoch {}]".format(epoch + 1))
            plt.xlabel("Epoch")
            plt.ylabel("Loss")
            plt.legend()

            plt.savefig('temp/Epoch-{}.png'.format(epoch + 1))
            pixmap = QPixmap('temp/Epoch-{}.png'.format(epoch + 1))
            scaled_pixmap = pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(scaled_pixmap)
            plt.close()

    def on_train_end(self, logs=None):
        self.progressbar.emit(100)
