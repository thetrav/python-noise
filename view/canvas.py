#!/usr/bin/env python

from PySide import QtGui, QtCore


class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Trav\'s Perlin Noise')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        qp.drawPoint(10, 10)
