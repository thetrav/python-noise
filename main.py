#!/usr/bin/env python

import sys
from canvas import Canvas
from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    Canvas()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
