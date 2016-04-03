#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore


# # QtGui.QCheckBox
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         cb = QtGui.QCheckBox('Show title', self)
#         cb.move(20, 20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QtGui.QCheckBox')
#         self.show()
#
#     def changeTitle(self, state):
#         if state == QtCore.Qt.Checked:
#             self.setWindowTitle('Checkbox')
#         else:
#             self.setWindowTitle('')


# # Toggle Button
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.col = QtGui.QColor(0, 0, 0)
#
#         redb = QtGui.QPushButton('Red', self)
#         redb.setCheckable(True)
#         redb.move(10, 10)
#         redb.clicked[bool].connect(self.setColor)
#
#         greenb = QtGui.QPushButton('Green', self)
#         greenb.setCheckable(True)
#         greenb.move(10, 60)
#         greenb.clicked[bool].connect(self.setColor)
#
#         blueb = QtGui.QPushButton('Blue', self)
#         blueb.setCheckable(True)
#         blueb.move(10, 110)
#         blueb.clicked[bool].connect(self.setColor)
#
#         self.square = QtGui.QFrame(self)
#         self.square.setGeometry(150, 20, 100, 100)
#         self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('Toggle Button')
#         self.show()
#
#     def setColor(self, pressed):
#         source = self.sender()
#
#         if pressed:
#             val = 255
#         else:
#             val = 0
#
#         if source.text() == 'Red':
#             self.col.setRed(val)
#         elif source.text() == 'Green':
#             self.col.setGreen(val)
#         else:
#             self.col.setBlue(val)
#
#         self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


# # QtGui.QSlider
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#         sld.setFocusPolicy(QtCore.Qt.NoFocus)
#         sld.setGeometry(30, 40, 100, 30)
#         sld.valueChanged[int].connect(self.changeValue)
#
#         self.label = QtGui.QLabel(self)
#         self.label.setPixmap(QtGui.QPixmap('mute.png'))
#         self.label.setGeometry(160, 40, 80, 30)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QtGui.QSlider')
#         self.show()
#
#     def changeValue(self, value):
#         if value == 0:
#             self.label.setPixmap(QtGui.QPixmap('mute.png'))
#         elif value > 0 and value <= 30:
#             self.label.setPixmap(QtGui.QPixmap('min.png'))
#         elif value > 30 and value <= 80:
#             self.label.setPixmap(QtGui.QPixmap('med.png'))
#         else:
#             self.label.setPixmap(QtGui.QPixmap('max.png'))


# # QtGui.QProgressBar
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.pbar = QtGui.QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#
#         self.btn = QtGui.QPushButton('Start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.timer = QtCore.QBasicTimer()
#         self.step = 0
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QtGui.QProgressBar')
#         self.show()
#
#     def timerEvent(self, e):
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#             return
#         self.step += 1
#         self.pbar.setValue(self.step)
#
#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')


# # QtGui.QCalendarWidget
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         cal = QtGui.QCalendarWidget(self)
#         cal.setGridVisible(True)
#         cal.move(20, 20)
#         cal.clicked[QtCore.QDate].connect(self.showDate)
#
#         self.lbl = QtGui.QLabel(self)
#         date = cal.selectedDate()
#         self.lbl.setText(date.toString())
#         self.lbl.move(130, 260)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('Calendar')
#         self.show()
#
#     def showDate(self, date):
#         self.lbl.setText(date.toString())


# # QtGui.QPixmap
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         hbox = QtGui.QHBoxLayout(self)
#         pixmap = QtGui.QPixmap('planet.png')
#
#         lbl = QtGui.QLabel(self)
#         lbl.setPixmap(pixmap)
#
#         hbox.addWidget(lbl)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('Planet')
#         self.show()


# # QtGui.QSplitter
# class Example(QtGui.QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         hbox = QtGui.QHBoxLayout(self)
#
#         topleft = QtGui.QFrame(self)
#         topleft.setFrameShape(QtGui.QFrame.StyledPanel)
#
#         topright = QtGui.QFrame(self)
#         topright.setFrameShape(QtGui.QFrame.StyledPanel)
#
#         bottom = QtGui.QFrame(self)
#         bottom.setFrameShape(QtGui.QFrame.StyledPanel)
#
#         splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#
#         splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QtGui.QSplitter')
#         self.show()
#
#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()


# QtGui.QComboBox
class Example(QtGui.QWidget):

    def __init__(self):
        super(type(self), self).__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QtGui.QLabel('Ubuntu', self)
        combo = QtGui.QComboBox(self)
        combo.addItems([
            'Ubuntu',
            'Mandriva',
            'Fedora',
            'Red Hat',
            'Gentoo'
        ])
        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()