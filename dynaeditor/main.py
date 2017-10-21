import sys
import json
from PySide2 import QtWidgets
from dynaeditor import utils
from dynaeditor.controller import Editor


def main():
    app = None
    if utils.in_maya_standalone():
        app = QtWidgets.QApplication([])

    editor = Editor()
    editor._view.show()

    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        items = json.load(file_in)

    mapped_items = []
    for item in items:
        mapped_items.append(utils.attr_mapping_to_dict(item))

    editor.set_editor_options(mapped_items)

    if utils.in_maya_standalone():
        sys.exit(app.exec_())

    return editor

if __name__ == '__main__':
    main()
