from maya import cmds
from PySide2 import QtWidgets, QtCore
from dynaeditor import const
from dynaeditor.view import EditorView
from dynaeditor.attributes.attribute import Attribute


class Editor(QtCore.QObject):
    _script_jobs = []

    def __init__(self):
        self._create_script_jobs()
        super(Editor, self).__init__()
        self._view = EditorView()
        self._attributes = []

    def selection_change(self):
        pass

    @QtCore.Slot
    def apply_attr_to_selection(self):
        pass

    def set_editor_options(self, attr_mappings):
        self.clear_attributes()
        for mapping in attr_mappings:
            if not Attribute.is_type_supported(mapping[const.ATTR_ARG_TYPE]):
                continue

            attribute = Attribute(**mapping)
            self._attributes.append(attribute)
            self._view.add_attr_widget(attribute.widget)

    def clear_attributes(self):
        self._attributes = []
        self._view.clear_editor()

    def _create_script_jobs(self):
        self._cleanup_script_jobs()
        job = cmds.scriptJob(event=["SelectionChanged", lambda :self.selection_change()])
        print job
        self._script_jobs.append(job)

    def _cleanup_script_jobs(self):
        for job in self._script_jobs:
            cmds.scriptJob(kill=job, force=True)
            print("removed ", job)

def main():
    app = QtWidgets.QApplication([])
    editor = Editor()
    editor._view.show()
    app.exec_()


if __name__ == '__main__':
    main()
