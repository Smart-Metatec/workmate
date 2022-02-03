import os
import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from database.model import Model

from widgetStyles.PushButton import IconButton, AppRunButton
from widgetStyles.styles import color, default, mode


class AppItem(QPushButton):
    app_clicked_signal = pyqtSignal(tuple)
    def __init__(self, app):
        super(AppItem, self).__init__()
        self.app = app
        self.setupUI()
        

        self.clicked.connect(self.app_clicked)

    def app_clicked(self):
        self.app_clicked_signal.emit(self.app)

    def create(self):
        return self
    
    def setupUI(self):
        self.setText(self.app[1])
        font = Model().read("settings")[0][2]
        self.setFont(QFont(font))