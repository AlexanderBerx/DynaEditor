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

    def set_options(self, options):
        self._qlist_attrs.clear()
        for status, attr in options:
            widget = QtWidgets.QCheckBox(str(attr))
            widget.setChecked(bool(status))
            item = QtWidgets.QListWidgetItem()
            self._qlist_attrs.addItem(item)
            self._qlist_attrs.setItemWidget(item, widget)

    def get_options(self):
        for index in range(self._qlist_attrs.count()):
            item = self._qlist_attrs.item(index)
            widget = ""


def main():
    app = QtWidgets.QApplication([])
    view = DisplayWidget()
    view.show()
    options = [(True, item) for item in range(5)]
    view.set_options(options)
    view.get_options()
    app.exec_()

if __name__ == '__main__':
    main()
