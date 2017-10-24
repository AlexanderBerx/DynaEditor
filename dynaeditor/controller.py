import sys
from maya import cmds
from PySide2 import QtWidgets, QtCore
from dynaeditor import const
from dynaeditor import utils
from dynaeditor import maya_utils
from dynaeditor.view import EditorView
from dynaeditor.job_manager import JobManager
from dynaeditor.attributes.attribute import Attribute


class Editor(QtCore.QObject):
    def __init__(self):
        super(Editor, self).__init__()

        self._job_manager = JobManager()
        self._job_manager.clean_up_jobs()
        self._job_manager.create_job(event=["SelectionChanged", lambda:self.selection_change()])

        self.check_for_existing_window()
        self.view = EditorView()
        self._connect_signals()

        self._attributes = []
        self._lock_type = False

    def _connect_signals(self):
        self.view.signal_lock_type.connect(self.toggle_type_lock)

    def check_for_existing_window(self):
        if cmds.window(EditorView.OBJ_NAME, exists=True):
            cmds.deleteUI(EditorView.OBJ_NAME, wnd=True)

    def selection_change(self):
        if self._lock_type == True:
            return
        self.update_to_selection()

    def update_to_selection(self):
        selected_shape = maya_utils.get_first_selected_shape()
        if not selected_shape:
            return

        # update to the shape node

    @QtCore.Slot()
    def apply_attr_to_selection(self):
        pass

    @QtCore.Slot()
    def toggle_type_lock(self):
        self._lock_type = not self._lock_type
        self.view.lock_type(self._lock_type)

    def set_editor_options(self, attr_mappings):
        self.clear_attributes()
        for mapping in attr_mappings:
            if not Attribute.is_type_supported(mapping[const.ATTR_ARG_TYPE]):
                continue

            attribute = Attribute(**mapping)
            self._attributes.append(attribute)
            self.view.add_attr_widget(attribute.widget)

    def clear_attributes(self):
        self._attributes = []
        self.view.clear_editor()


def main():
    app = None
    if utils.in_maya_standalone():
        app = QtWidgets.QApplication([])

    attr_editor = Editor()
    attr_editor.view.show()

    if utils.in_maya_standalone():
        sys.exit(app.exec_())

    return attr_editor


if __name__ == '__main__':
    editor = main()
