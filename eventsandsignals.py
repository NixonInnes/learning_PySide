#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore

# # Signal & Slot
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         lcd = QtGui.QLCDNumber(self)
#         sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & Slot')
#         self.show()


# # Overriding handlers
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Event Handler')
#         self.show()
#
#     def keyPressEvent(self, e):
#         if e.key() == QtCore.Qt.Key_Escape:
#             self.close()


# # Event Sender
# class Example(QtGui.QMainWindow):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         btn1 = QtGui.QPushButton('Button 1', self)
#         btn1.move(30, 50)
#
#         btn2 = QtGui.QPushButton('Button 2', self)
#         btn2.move(150, 50)
#
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event Sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' was pressed')


# Emitting Signals
class Communicate(QtCore.QObject):
    closeApp = QtCore.Signal()


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()