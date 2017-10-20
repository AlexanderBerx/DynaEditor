import json
from PySide2 import QtWidgets
from dynaeditor import const
from dynaeditor import utils
from dynaeditor.view import EditorView
from dynaeditor.attributes.attribute import Attribute


class Editor(object):
    def __init__(self):
        self._view = EditorView()
        self._view.show()
        self._editors = []

    def selection_change(self):
        pass

    def set_editor_options(self, attr_mapping):
        for item in attr_mapping:
            # first arg is the type, check if supported before proceeding
            if not item[0] in const.SUPPORTED_ATTR_TYPES:
                continue
            args = utils.attr_mapping_to_dict(item)
            attr = Attribute(**args)
            print(attr)


def main():
    app = QtWidgets.QApplication([])
    editor = Editor()
    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        mapping = json.load(file_in)
    editor.set_editor_options(mapping)
    app.exec_()


if __name__ == '__main__':
    main()
