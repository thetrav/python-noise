#!/usr/bin/env python

import sys
from PySide import QtGui
from numpy import array
from view import View
from perlin import Perlin


def main():
    width = 300
    height = 300
    app = QtGui.QApplication(sys.argv)
    perlin = Perlin()
    print "generating image"
    image = [[int(perlin.value(array([x, y])) * 200)
              for y in range(width)] for x in range(height)]
    print "rendering frame"
    # NOTE: View is garbage collected if I don't extract to a variable
    v = View(image, width, height)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
