import sys
from PySide2 import QtWidgets
from dynaeditor import utils
from dynaeditor.controller import Editor


def main():
    app = None
    if utils.in_maya_standalone():
        app = QtWidgets.QApplication([])

    editor = Editor()
    editor.view.show()

    if utils.in_maya_standalone():
        sys.exit(app.exec_())

    return editor

if __name__ == '__main__':
    editor = main()
