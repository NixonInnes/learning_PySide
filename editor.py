#!/usr/bin/env python3

import sys, random
from PySide import QtGui, QtCore


class Editor(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Text Editor')
        self.center()

        self.editor = QtGui.QTextEdit()
        self.setCentralWidget(self.editor)

        statusbar = self.statusBar()
        menubar = self.menuBar()
        self.filemenu = menubar.addMenu('&File')
        self.helpmenu = menubar.addMenu('&Help')
        self.add_actions()

        self.show()
        statusbar.showMessage('Ready')

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def add_actions(self):
        do_fopen = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        do_fopen.setShortcut('Ctrl+O')
        do_fopen.setStatusTip('Open file')
        do_fopen.triggered.connect(self.fopenDialog)
        self.filemenu.addAction(do_fopen)

        do_fsave = QtGui.QAction(QtGui.QIcon('save.png'), 'Save', self)
        do_fsave.setShortcut('Ctrl+S')
        do_fsave.setStatusTip('Save file')
        do_fsave.triggered.connect(self.fsaveDialog)
        self.filemenu.addAction(do_fsave)

        do_exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        do_exit.setShortcut('Ctrl+Q')
        do_exit.setStatusTip('Exit application')
        do_exit.triggered.connect(self.close)
        self.filemenu.addAction(do_exit)


    def fopenDialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        with open(fname, 'r') as file:
            data = file.read()
            self.editor.setText(data)

    def fsaveDialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Save File', '/home')
        with open(fname, 'w') as file:
            data = self.editor.text
            file.write(data)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure you want to Quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()