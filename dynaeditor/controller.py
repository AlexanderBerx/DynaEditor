from PySide2 import QtWidgets
from dynaeditor import const
from dynaeditor.view import EditorView
from dynaeditor.attributes.attribute import Attribute


class Editor(object):
    def __init__(self):
        self._view = EditorView()
        self._attributes = []

    def selection_change(self):
        pass

    def set_editor_options(self, attr_mappings):
        self.clear_attributes()
        for mapping in attr_mappings:
            if not Attribute.is_type_supported(mapping[const.ATTR_ARG_TYPE]):
                continue
            print mapping
            attribute = Attribute(**mapping)
            # self._attributes.append()

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
