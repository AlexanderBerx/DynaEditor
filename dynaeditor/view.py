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
        layout_main.addWidget(self._create_type_widget())

    def _create_type_widget(self):
        type_widget = QtWidgets.QWidget()
        type_layout = QtWidgets.QHBoxLayout()
        type_widget.setLayout(type_layout)

        type_layout.addWidget(QtWidgets.QLabel("Object Type:"))
        self._lbl_obj_type = QtWidgets.QLabel()
        self._lbl_obj_type.setTextFormat(QtCore.Qt.RichText)
        type_layout.addWidget(self._lbl_obj_type)
        self._lock_type_btn = QtWidgets.QPushButton()
        type_layout.addWidget(self._lock_type_btn)
        return type_widget

    def set_m_object_type(self, _type):
        self._lbl_obj_type.setText("<b>{}</b>".format(_type))

    def lock_type(self, lock=True):
        if lock:
            self._lbl_obj_type.setEnabled(False)
        else:
            self._lbl_obj_type.setEnabled(True)


def main():
    app = QtWidgets.QApplication([])
    view = EditorView()
    view.set_m_object_type("test")
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
