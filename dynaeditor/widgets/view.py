from PySide2 import QtWidgets, QtCore, QtGui
from dynaeditor.utils import general_utils


class EditorView(QtWidgets.QWidget):
    TITLE = "Dynamic Attribute Editor"
    OBJ_NAME = "dynaAttrEditor"
    signal_lock_type = QtCore.Signal()

    def __init__(self, parent=None):
        if not parent:
            parent = general_utils.get_maya_main_window()

        super(EditorView, self).__init__(parent=parent)
        self.setWindowTitle(self.TITLE)
        self.setObjectName(self.OBJ_NAME)
        self.setWindowFlags(QtCore.Qt.Window)

        self._init_ui()
        self.center_to_parent()

    def _init_ui(self):
        self._lock_icon = QtGui.QIcon(":/icon_lock.png")
        self._unlock_icon = QtGui.QIcon(":/icon_unlock.png")
        layout_main = QtWidgets.QVBoxLayout()
        self.setLayout(layout_main)
        layout_main.addWidget(self._create_header_widget())
        layout_main.addWidget(self._create_editor_widget())

    def center_to_parent(self):
        if self.parent():
            parent_pos = self.parent().pos()
            parent_width = self.parent().width()
            parent_height = self.parent().height()

            parent_center = [parent_pos.x() + parent_width / 2, parent_pos.y() + parent_height / 2]
            self.move(QtCore.QPoint(parent_center[0] - self.width() / 2, parent_center[1] - self.height() / 2))

    def _create_header_widget(self):
        widget_header = QtWidgets.QWidget()
        layout_header = QtWidgets.QHBoxLayout()
        widget_header.setLayout(layout_header)
        layout_header.addWidget(QtWidgets.QLabel("Type:"))
        self._lbl_display_type = QtWidgets.QLabel("<b>----</b>")
        layout_header.addWidget(self._lbl_display_type)

        self._btn_lock_type = QtWidgets.QPushButton()
        self._btn_lock_type.setIcon(self._lock_icon)
        self._btn_lock_type.setFixedSize(self._btn_lock_type.iconSize()*1.8)
        self._btn_lock_type.clicked.connect(self.signal_lock_type)

        layout_header.addWidget(self._btn_lock_type)
        return widget_header

    def _create_editor_widget(self):
        self.editor = QtWidgets.QListWidget()
        self.editor.setAlternatingRowColors(True)
        return self.editor

    def set_display_type(self, _type):
        self._lbl_display_type.setText("<b>{}</b>".format(_type))

    def clear_editor(self):
        self.editor.clear()

    def add_attr_widget(self, widget):
        """
        :param QtWidgets.QWidget widget:
        :return:
        """
        item = QtWidgets.QListWidgetItem(self.editor)
        item.setSizeHint(widget.sizeHint())
        self.editor.setItemWidget(item, widget)

    def lock_type(self, lock=True):
        if lock:
            self._lbl_display_type.setEnabled(False)
            self._btn_lock_type.setIcon(self._unlock_icon)
        else:
            self._lbl_display_type.setEnabled(True)
            self._btn_lock_type.setIcon(self._lock_icon)


def main():
    app = QtWidgets.QApplication([])
    view = EditorView()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
