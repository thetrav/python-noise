from PySide import QtGui


class View(QtGui.QWidget):
    def __init__(self, image, w, h):
        super(View, self).__init__()
        self.w = w
        self.h = h
        self.pixmap = QtGui.QPixmap(w, h)
        self.drawPoints(QtGui.QPainter(self.pixmap), image)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle('Perlin')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawPixmap(self.contentsRect(), self.pixmap)
        qp.end()

    # TODO: find a faster rendering option.
    def drawPoints(self, qp, image):
        for x in range(self.w):
            for y in range(self.h):
                noise = image[x][y]
                qp.setPen(QtGui.QColor(noise, noise, noise))
                qp.drawPoint(x, y)
