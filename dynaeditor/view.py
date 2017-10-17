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

    def set_attr_widgets(self, attrs):
        pass

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
    view.set_m_object_type("test")
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
