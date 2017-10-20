from PySide2 import QtWidgets, QtCore


class EditorView(QtWidgets.QWidget):
    TITLE = "Dynamic Attribute Editor"
    OBJ_NAME = "dynaAttrEditor"

    def __init__(self):
        super(EditorView, self).__init__()
        self.setWindowTitle(self.TITLE)
        self.setObjectName(self.OBJ_NAME)

        self._lock_type = False
        self._init_ui()

    def _init_ui(self):
        layout_main = QtWidgets.QVBoxLayout()
        self.setLayout(layout_main)
        layout_main.addWidget(self._create_header_widget())
        layout_main.addWidget(self._create_editor_widget())

    def _create_header_widget(self):
        widget_header = QtWidgets.QWidget()
        layout_header = QtWidgets.QHBoxLayout()
        widget_header.setLayout(layout_header)
        layout_header.addWidget(QtWidgets.QLabel("Type:"))
        self._lbl_display_type = QtWidgets.QLabel("----")
        layout_header.addWidget(self._lbl_display_type)
        self._btn_lock_type = QtWidgets.QPushButton("Lock")
        layout_header.addWidget(self._btn_lock_type)
        return widget_header

    def _create_editor_widget(self):
        editor = QtWidgets.QListWidget()
        return editor

    def set_display_type(self, _type):
        self._lbl_display_type.setText("<b>{}</b>".format(_type))

    def lock_type(self, lock=True):
        if lock:
            self._lbl_obj_type.setEnabled(False)
        else:
            self._lbl_obj_type.setEnabled(True)


def main():
    app = QtWidgets.QApplication([])
    view = EditorView()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
