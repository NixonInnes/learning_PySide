#!/usr/bin/env python3

import sys
from PySide import QtGui

# # QtGui.QInputDialog
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.btn = QtGui.QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le = QtGui.QLineEdit(self)
#         self.le.move(130, 22)
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Input Dialog')
#         self.show()
#
#     def showDialog(self):
#         text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
#
#         if ok:
#             self.le.setText(str(text))


# # QtGui.QColorDialog
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         col = QtGui.QColor(0, 0, 0)
#
#         self.btn = QtGui.QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#
#         self.btn.clicked.connect(self.showDialog)
#
#         self.frm = QtGui.QFrame(self)
#         self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)
#
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Colour Dialog')
#         self.show()
#
#     def showDialog(self):
#         col = QtGui.QColorDialog.getColor()
#
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


# QtGui.QFontDialog
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton('Dialog')
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()