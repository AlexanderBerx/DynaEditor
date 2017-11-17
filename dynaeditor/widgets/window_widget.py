from PySide2 import QtCore, QtWidgets, QtGui
from dynaeditor.widgets.editor_view import EditorView
from dynaeditor.utils import general_utils
from dynaeditor.prefs_manager import PrefsManager


class EditorWidget(QtWidgets.QWidget):
    TITLE = "Dynamic Attribute Editor"
    OBJ_NAME = "dynaAttrEditor"
    signal_lock_type = QtCore.Signal()
    signal_display_prefs  = QtCore.Signal()
    signal_apply_attr = QtCore.Signal(str, str, str)
    signal_restrict_to_type = QtCore.Signal(bool)
    signal_affect_children = QtCore.Signal(bool)
    signal_window_close = QtCore.Signal()

    def __init__(self, parent=None):
        if not parent:
            parent = general_utils.get_maya_main_window()

        super(EditorWidget, self).__init__(parent=parent)
        self.setWindowTitle(self.TITLE)
        self.setObjectName(self.OBJ_NAME)
        self.setWindowFlags(QtCore.Qt.Window)

        self._init_ui()
        self.center_to_parent()
        self.load_prefs()

    def closeEvent(self, event):
        self.save_prefs()
        self.signal_window_close.emit()
        self.deleteLater()

    def save_prefs(self):
        prefs_manager = PrefsManager()
        prefs_manager.window_pos = self.pos()
        prefs_manager.window_size = self.size()

    def load_prefs(self):
        prefs_manager = PrefsManager()
        if prefs_manager.window_pos:
            self.move(prefs_manager.window_pos)
        if prefs_manager.window_size:
            self.resize(prefs_manager.window_size)

    def _init_ui(self):
        self._lock_icon = QtGui.QIcon(":/icon_lock.png")
        self._unlock_icon = QtGui.QIcon(":/icon_unlock.png")

        layout_main = QtWidgets.QVBoxLayout()
        layout_main.setMargin(0)
        self.setLayout(layout_main)

        layout_main.addWidget(self._create_menu_bar())
        layout_main.addWidget(self._create_header_widget())
        layout_main.addWidget(self._create_editor_widget())
        layout_main.addWidget(self._create_status_bar_widget())

    def center_to_parent(self):
        if self.parent():
            parent_pos = self.parent().pos()
            parent_width = self.parent().width()
            parent_height = self.parent().height()

            parent_center = [parent_pos.x() + parent_width / 2, parent_pos.y() + parent_height / 2]
            self.move(QtCore.QPoint(parent_center[0] - self.width() / 2, parent_center[1] - self.height() / 2))

    def _create_menu_bar(self):
        self._menu_bar = QtWidgets.QMenuBar()
        prefs_menu = QtWidgets.QMenu("Preferences")
        prefs_menu.setToolTipsVisible(True)
        self._menu_bar.addMenu(prefs_menu)

        display_action = QtWidgets.QAction("Item Display", prefs_menu)
        display_action.setToolTip("Attribute item visibility preference's")
        display_action.triggered.connect(self.signal_display_prefs.emit)
        prefs_menu.addAction(display_action)

        restrict_action = QtWidgets.QAction("Restrict to current type", prefs_menu, checkable=True)
        restrict_action.setToolTip("Restrict the editor to only apply attributes\n"
                                   "to objects of the same type as currently set")
        restrict_action.setChecked(True)
        restrict_action.triggered.connect(lambda : self.signal_restrict_to_type.emit(restrict_action.isChecked()))
        prefs_menu.addAction(restrict_action)

        affect_children_action = QtWidgets.QAction("Affect children", prefs_menu, checkable=True)
        affect_children_action.setToolTip("applies the attribute to all children of"
                                         "the current selection")
        affect_children_action.setChecked(True)
        affect_children_action.triggered.connect(lambda : self.signal_affect_children.emit(affect_children_action.isChecked()))
        prefs_menu.addAction(affect_children_action)

        self._menu_bar.addMenu("Help")
        return self._menu_bar

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
        self.editor = EditorView()
        self.editor.signal_apply_attr[str, str, str].connect(self._emit_apply_attr)
        return self.editor

    def _create_status_bar_widget(self):
        self._status_bar = QtWidgets.QStatusBar()
        return self._status_bar

    def set_display_type(self, type_):
        self._lbl_display_type.setText("<b>{}</b>".format(type_))

    def set_attr_model(self, model):
        """
        :return: QtCore.QAbstractListModel
        """
        self.editor.setModel(model)

    def set_status_text(self, text, time_out=0):
        self._status_bar.showMessage(str(text), time_out)

    @QtCore.Slot(str, str, str)
    def _emit_apply_attr(self, attr_name, attr_value, attr_type):
        self.signal_apply_attr.emit(attr_name, attr_value, attr_type)

    def lock_type(self, lock=True):
        if lock:
            self._lbl_display_type.setEnabled(False)
            self._btn_lock_type.setIcon(self._unlock_icon)
        else:
            self._lbl_display_type.setEnabled(True)
            self._btn_lock_type.setIcon(self._lock_icon)


def main():
    app = QtWidgets.QApplication([])
    view = EditorWidget()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
