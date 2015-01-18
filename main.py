#!/usr/bin/env python

import sys
import view
from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    view.Canvas()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
