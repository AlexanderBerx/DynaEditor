from PySide2 import QtWidgets, QtCore


class DisplayWidget(QtWidgets.QWidget):
    TITLE = "Hide/Show attrs"
    OBJ_NAME = "displayWidget"

    def __init__(self):
        super(DisplayWidget, self).__init__()
        self.setWindowTitle(self.TITLE)
        self.setObjectName(self.OBJ_NAME)
        self.setWindowFlags(QtCore.Qt.Window)

        self._init_ui()

    def _init_ui(self):
        layout_main = QtWidgets.QVBoxLayout()
        self.setLayout(layout_main)

        self._qlist_attrs = QtWidgets.QListWidget()
        layout_main.addWidget(self._qlist_attrs)

        layout_options = QtWidgets.QHBoxLayout()
        self._btn_confirm = QtWidgets.QPushButton("Confirm")
        layout_options.addWidget(self._btn_confirm)
        self._btn_cancel = QtWidgets.QPushButton("Cancel")
        layout_options.addWidget(self._btn_cancel)
        layout_main.addLayout(layout_options)


def main():
    app = QtWidgets.QApplication([])
    view = DisplayWidget()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
