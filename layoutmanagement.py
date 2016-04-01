#!/usr/bin/env python3

import sys
from PySide import QtGui


# # Absolute Positioning
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         label1 = QtGui.QLabel('Nixcode', self)
#         label1.move(15, 10)
#
#         label2 = QtGui.QLabel('tutorials', self)
#         label2.move(35, 40)
#
#         label3 = QtGui.QLabel('for programmers', self)
#         label3.move(55, 70)
#
#         self.setGeometry(300, 300, 250, 100)
#         self.setWindowTitle('Absolute')
#         self.show()


# # Box/Stretch Positioning
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         okButton = QtGui.QPushButton('OK')
#         cancelButton = QtGui.QPushButton('Cancel')
#
#         hbox = QtGui.QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QtGui.QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Buttons')
#         self.show()


# # Grid Layout
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5',
#                  '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
#         grid = QtGui.QGridLayout()
#         j = 0
#         pos = [(0, 0), (0, 1), (0, 2), (0, 3),
#                (1, 0), (1, 1), (1, 2), (1, 3),
#                (2, 0), (2, 1), (2, 2), (2, 3),
#                (3, 0), (3, 1), (3, 2), (3, 3),
#                (4, 0), (4, 1), (4, 2), (4, 3)]
#
#         for i in names:
#             button = QtGui.QPushButton(i)
#             if j == 2:
#                 grid.addWidget(QtGui.QLabel(''), 0, 2)
#             else:
#                 grid.addWidget(button, pos[j][0], pos[j][1])
#             j += 1
#
#         self.setLayout(grid)
#         self.move(300, 150)
#         self.setWindowTitle('Calculator')
#         self.show()


# Grid Layout 2
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()