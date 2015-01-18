from PySide import QtGui


class View(QtGui.QWidget):
    def __init__(self, image):
        super(View, self).__init__()
        self.image = image
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, len(self.image), len(self.image[0]))
        self.setWindowTitle('Perlin')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    # TODO: find a faster rendering option.
    def drawPoints(self, qp):
        size = self.size()
        for x in range(size.width()):
            for y in range(size.height()):
                noise = self.image[x][y]
                qp.setPen(QtGui.QColor(noise, noise, noise))
                qp.drawPoint(x, y)
