from maya import cmds
from PySide2 import QtWidgets, QtCore
from dynaeditor import const
from dynaeditor.view import EditorView
from dynaeditor.job_manager import JobManager
from dynaeditor.attributes.attribute import Attribute


class Editor(QtCore.QObject):
    def __init__(self):
        super(Editor, self).__init__()

        self.job_manager = JobManager()
        self.job_manager.clean_up_jobs()
        self.job_manager.create_job(event=["SelectionChanged", lambda :self.selection_change()])

        self.check_for_existing_window()
        self._view = EditorView()
        self._attributes = []

    def check_for_existing_window(self):
        if cmds.window(EditorView.OBJ_NAME, exists=True):
            cmds.deleteUI(EditorView.OBJ_NAME, wnd=True)

    def selection_change(self):
        print("change")

    @QtCore.Slot()
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


def main():
    app = QtWidgets.QApplication([])
    editor = Editor()
    editor._view.show()
    app.exec_()


if __name__ == '__main__':
    main()
