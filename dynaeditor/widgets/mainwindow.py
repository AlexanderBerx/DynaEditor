from PySide2 import QtCore, QtWidgets, QtGui
from dynaeditor.widgets.editorview import EditorView
from dynaeditor.utils import general
from dynaeditor.prefsmanager import PrefsManager


class EditorWindow(QtWidgets.QWidget):
    """
    EditorWindow class, inherits from QtWidgets.QWidget
    main window of the app
    """
    TITLE = "Dynamic Attribute Editor"
    OBJ_NAME = "dynaAttrEditor"
    signal_lock_type = QtCore.Signal()
    signal_display_prefs = QtCore.Signal()
    signal_apply_attr = QtCore.Signal(str, str, str)
    signal_search = QtCore.Signal(str)
    signal_window_close = QtCore.Signal()

    def __init__(self, parent=None):
        if not parent:
            parent = general.get_maya_main_window()

        super(EditorWindow, self).__init__(parent=parent)
        self.setWindowTitle(self.TITLE)
        self.setObjectName(self.OBJ_NAME)
        self.setWindowFlags(QtCore.Qt.Window)

        self._init_ui()
        self.center_to_parent()
        self.load_prefs()

    def closeEvent(self, event):
        """
        overwritten method from QtWidgets.QWidget
        saves the prefs on window close and emits signal_window_close
        :param event:
        :return: None
        """
        self.save_prefs()
        self.signal_window_close.emit()
        self.deleteLater()

    def save_prefs(self):
        """
        saves the window preferences
        :return: None
        """
        prefs_manager = PrefsManager()
        prefs_manager.window_pos = self.pos()
        prefs_manager.window_size = self.size()
        prefs_manager.affect_children = self.affect_children()
        prefs_manager.restrict_to_type = self.restrict_to_type()

    def load_prefs(self):
        """
        loads the window preferences
        :return: None
        """
        prefs_manager = PrefsManager()
        if prefs_manager.window_pos:
            self.move(prefs_manager.window_pos)
        if prefs_manager.window_size:
            self.resize(prefs_manager.window_size)
        self._affect_children_action.setChecked(prefs_manager.affect_children)
        self._restrict_action.setChecked(prefs_manager.restrict_to_type)

    def _init_ui(self):
        """
        initialises the ui
        :return: None
        """
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
        """
        centers the window to it's parent
        :return: None
        """
        if self.parent():
            parent_pos = self.parent().pos()
            parent_width = self.parent().width()
            parent_height = self.parent().height()

            parent_center = [parent_pos.x() + parent_width / 2, parent_pos.y() + parent_height / 2]
            self.move(QtCore.QPoint(parent_center[0] - self.width() / 2, parent_center[1] - self.height() / 2))

    def _create_menu_bar(self):
        """
        creates the menu bar
        :return: QtWidgets.QMenuBar
        """
        self._menu_bar = QtWidgets.QMenuBar()
        prefs_menu = QtWidgets.QMenu("Preferences")
        prefs_menu.setToolTipsVisible(True)
        self._menu_bar.addMenu(prefs_menu)

        display_action = QtWidgets.QAction("Item Display", prefs_menu)
        display_action.setToolTip("Attribute item visibility preference's")
        display_action.triggered.connect(self.signal_display_prefs.emit)
        prefs_menu.addAction(display_action)

        self._restrict_action = QtWidgets.QAction("Restrict to current type", prefs_menu, checkable=True)
        self._restrict_action.setToolTip("Restrict the editor to only apply attributes\n"
                                         "to objects of the same type as currently set")
        self._restrict_action.setChecked(True)
        prefs_menu.addAction(self._restrict_action)

        self._affect_children_action = QtWidgets.QAction("Affect children", prefs_menu, checkable=True)
        self._affect_children_action.setToolTip("applies the attribute to all children of"
                                                "the current selection")
        self._affect_children_action.setChecked(True)
        prefs_menu.addAction(self._affect_children_action)

        # TODO: Implement help menu
        # self._menu_bar.addMenu("Help")
        return self._menu_bar

    def _create_header_widget(self):
        """
        creates the header widget
        :return: QtWidgets.QWidget
        """
        widget_header = QtWidgets.QWidget()
        layout_header = QtWidgets.QVBoxLayout()
        layout_header.setMargin(0)
        widget_header.setLayout(layout_header)

        layout_type = QtWidgets.QHBoxLayout()
        layout_type.addSpacerItem(QtWidgets.QSpacerItem(10, 10))
        layout_header.addLayout(layout_type)
        layout_type.addWidget(QtWidgets.QLabel("Type:"))
        self._lbl_display_type = QtWidgets.QLabel("<b>----</b>")
        layout_type.addWidget(self._lbl_display_type)

        self._btn_lock_type = QtWidgets.QPushButton()
        self._btn_lock_type.setIcon(self._lock_icon)
        self._btn_lock_type.setFixedSize(self._btn_lock_type.iconSize() * 1.8)
        self._btn_lock_type.clicked.connect(self.signal_lock_type)

        layout_type.addWidget(self._btn_lock_type)
        layout_type.addSpacerItem(QtWidgets.QSpacerItem(10, 10))

        self._txt_search = QtWidgets.QLineEdit()
        self._txt_search.setPlaceholderText("Search")
        self._txt_search.textChanged[str].connect(self.signal_search)
        layout_header.addWidget(self._txt_search)
        return widget_header

    def _create_editor_widget(self):
        """
        creates the editor widget
        :return: QtWidgets.QWidget
        """
        self.editor = EditorView()
        self.editor.signal_apply_attr[str, str, str].connect(self._emit_apply_attr)
        return self.editor

    def _create_status_bar_widget(self):
        """
        creates the status bar widget
        :return: QtWidgets.QWidget
        """
        self._status_bar = QtWidgets.QStatusBar()
        return self._status_bar

    def set_display_type(self, text):
        """
        sets the display text in the header widget
        :param str text:
        :return: None
        """
        self._lbl_display_type.setText("<b>{}</b>".format(text))

    def set_attr_model(self, model):
        """
        sets the editor model
        :param QtCore.QAbstractListModel model:
        :return:
        """
        self.editor.setModel(model)

    def set_status_text(self, text, time_out=0):
        """
        sets the status text to be displayed
        :param str text: text to be displayed
        :param int time_out: time out of the display text
        :return: None
        """
        self._status_bar.showMessage(str(text), time_out)

    @QtCore.Slot(str, str, str)
    def _emit_apply_attr(self, attr_name, attr_value, attr_type):
        """
        slot to further emit when an attribute is being applied,
        emits signal_apply_attr
        :param str attr_name:
        :param str attr_value:
        :param str attr_type:
        :return: None
        """
        self.signal_apply_attr.emit(attr_name, attr_value, attr_type)

    def lock_type(self, lock=True):
        """
        sets the lock type
        :param bool lock:
        :return: None
        """
        if lock:
            self._lbl_display_type.setEnabled(False)
            self._btn_lock_type.setIcon(self._unlock_icon)
        else:
            self._lbl_display_type.setEnabled(True)
            self._btn_lock_type.setIcon(self._lock_icon)

    def restrict_to_type(self):
        """
        :return: bool
        """
        return self._restrict_action.isChecked()

    def affect_children(self):
        """
        :return: bool
        """
        return self._affect_children_action.isChecked()


def main():
    app = QtWidgets.QApplication([])
    view = EditorWindow()
    view.show()
    app.exec_()


if __name__ == '__main__':
    main()
