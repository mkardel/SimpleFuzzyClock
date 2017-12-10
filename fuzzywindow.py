"""
Copyright Matthias Kardel 2017-12-10
"""

from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import QPoint, Qt

from fuzzyclock import FuzzyClock


class SimpleFuzzyClockWindow(QMainWindow):

    def __init__(self, fuzzy_clock=None, size=(190, 35)):
        super().__init__()

        if fuzzy_clock is None:
            self.fuzzy_clock = FuzzyClock()
        else:
            self.fuzzy_clock = fuzzy_clock

        self.main_widget = QMainWindow(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setFixedSize(size[0], size[1])

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgb(0,0,0);"
                                 "color: rgb(0,255,0);"
                                 "font: bold 14pt 'Times New Roman';")

        self.label.setGeometry(0, 0, size[0], size[1])
        self.set_text(text=self.fuzzy_clock.get_time())

        self.old_pos = self.pos()

    def set_text(self, text=""):
        self.label.setText(text)
        self.show()

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        movement = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + movement.x(), self.y() + movement.y())
        self.old_pos = event.globalPos()

    def update_label(self):
        self.fuzzy_clock.update()
        self.set_text(self.fuzzy_clock.get_time())
