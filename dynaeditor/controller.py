import sys
import json
import logging
from maya import cmds
from PySide2 import QtCore, QtWidgets
from dynaeditor.job_manager import JobManager
from dynaeditor.utils import general_utils, maya_utils
from dynaeditor.widgets import window_widget
reload(window_widget)
from dynaeditor.widgets.window_widget import EditorWidget
from dynaeditor import model
reload(model)
from dynaeditor.model import EditorModel, EditorProxyModel


class Editor(QtCore.QObject):
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.debug("Creating Editor Instance")
        super(Editor, self).__init__()

        # create JobManager instance for managing script jobs
        self._job_manager = JobManager()
        self._job_manager.clean_up_jobs()
        self._job_manager.create_job(event=["SelectionChanged", lambda:self.selection_change()])

        self.check_for_existing_window()
        self.view = EditorWidget()
        self.model = EditorModel()
        self.proxy_model = EditorProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.view.set_attr_model(self.proxy_model)
        self._connect_signals()
        self._lock_type = False

        logger.debug("Created Editor instance")

    def _connect_signals(self):
        # from view
        self.view.signal_lock_type.connect(self.toggle_type_lock)
        self.view.signal_display_prefs.connect(self.display_prefs)
        self.view.signal_apply_attr[str, str, str].connect(self.apply_attr_to_selection)
        self.view.signal_restrict_to_type[bool].connect(self.restrict_to_type)
        self.view.signal_affect_children[bool].connect(self.affect_children)
        self.view.signal_window_close.connect(self.window_close)
        # from model
        self.model.signal_type_changed[str].connect(self.type_change)

    @staticmethod
    def check_for_existing_window():
        if cmds.window(EditorWidget.OBJ_NAME, exists=True):
            cmds.deleteUI(EditorWidget.OBJ_NAME, wnd=True)

    def selection_change(self):
        if self._lock_type:
            return
        self.update_to_selection()

    def update_to_selection(self):
        node = maya_utils.get_first_selected_node()
        if not node:
            return

        self.view.set_status_text("Updating to type: {}".format(cmds.objectType(node)), 1000)
        self.model.set_to_node(node)

    @QtCore.Slot(str, str, str)
    def apply_attr_to_selection(self, name, value, _type):
        logger = logging.getLogger(__name__)
        logger.info("Applying attr: {}".format(name))
        logger.info("_type: {}".format(_type))
        logger.info("value: {}".format(value))
        value = json.loads(value)
        self.view.set_status_text(name, 2000)

    @QtCore.Slot()
    def toggle_type_lock(self):
        self._lock_type = not self._lock_type
        self.view.lock_type(self._lock_type)

    @QtCore.Slot()
    def display_prefs(self):
        self.prefs_view = QtWidgets.QListView(self.view)
        self.prefs_view.setWindowTitle("Item Display")
        self.prefs_view.setWindowFlags(QtCore.Qt.Window)
        self.prefs_view.setModel(self.model)
        self.prefs_view.show()

    @QtCore.Slot(bool)
    def restrict_to_type(self, restrict):
        self.model.restrict_to_type = restrict

    @QtCore.Slot(bool)
    def affect_children(self, affect):
        self.model.affect_children = affect

    @QtCore.Slot(str)
    def type_change(self, type_):
        self.view.set_display_type(type_)

    @QtCore.Slot()
    def window_close(self):
        if self.prefs_view:
            self.prefs_view.close()


def main():
    app = None
    if general_utils.in_maya_standalone():
        app = QtWidgets.QApplication([])

    attr_editor = Editor()
    attr_editor.view.show()

    if general_utils.in_maya_standalone():
        sys.exit(app.exec_())

    return attr_editor


if __name__ == '__main__':
    editor = main()
