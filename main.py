"""
Copyright Matthias Kardel 2017-12-10
"""

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

import sys

from fuzzywindow import SimpleFuzzyClockWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = SimpleFuzzyClockWindow()

    timer = QTimer()
    timer.timeout.connect(my_window.update_label)
    every_minute = 60 * 1000
    timer.start(every_minute)

    sys.exit(app.exec_())
