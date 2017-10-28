import json
import logging
import sys

from PySide2 import QtWidgets, QtCore
from dynaeditor import attr_query
from dynaeditor import maya_utils
from dynaeditor import utils
from dynaeditor.job_manager import JobManager
from dynaeditor.widgets.view import EditorView
from dynaeditor.attributes.attribute import Attribute
from dynaeditor.attributes.attr_type_error import AttrTypeError
from maya import cmds





class Editor(QtCore.QObject):
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.debug("Creating Editor Instance")
        super(Editor, self).__init__()

        self._job_manager = JobManager()
        self._job_manager.clean_up_jobs()
        self._job_manager.create_job(event=["SelectionChanged", lambda:self.selection_change()])

        self.check_for_existing_window()
        self.view = EditorView()
        self._connect_signals()

        self._attributes = []
        self._lock_type = False
        logger.debug("Created Editor instance")

    def _connect_signals(self):
        self.view.signal_lock_type.connect(self.toggle_type_lock)

    @staticmethod
    def check_for_existing_window():
        if cmds.window(EditorView.OBJ_NAME, exists=True):
            cmds.deleteUI(EditorView.OBJ_NAME, wnd=True)

    def selection_change(self):
        if self._lock_type:
            return
        self.update_to_selection()

    def update_to_selection(self):
        selected_shape = maya_utils.get_first_selected_shape()
        if not selected_shape:
            return
        # update to the shape node
        self.set_editor_options(attr_query.iter_obj_attrs_mapped(selected_shape))

    @QtCore.Slot(str, str, str)
    def apply_attr_to_selection(self, name, _type, value):
        logger = logging.getLogger(__name__)
        logger.info("Applying attr: {}".format(name))
        logger.info("_type: {}".format(_type))
        logger.info("value: {}".format(value))
        value = json.loads(value)

    @QtCore.Slot()
    def toggle_type_lock(self):
        self._lock_type = not self._lock_type
        self.view.lock_type(self._lock_type)

    def set_editor_options(self, attr_mappings):
        self.clear_attributes()
        logger = logging.getLogger(__name__)
        for mapping in attr_mappings:
            try:
                attribute = Attribute(**mapping)
            # skip not implemented types
            except AttrTypeError as e:
                logger.warning(e)
                continue

            attribute.signal_apply_attr[str, str, str].connect(self.apply_attr_to_selection)
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


    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)
    mapped_data = [utils.key_map_config(data) for data in test_data]

    attr_editor.set_editor_options(mapped_data)


    if utils.in_maya_standalone():
        sys.exit(app.exec_())

    return attr_editor


if __name__ == '__main__':
    editor = main()
