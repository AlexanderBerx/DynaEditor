import json
from PySide2 import QtWidgets
from dynaeditor.controller import Editor


def test_full():
    # TODO: implement check to see if an QApplication is already running
    app = QtWidgets.QApplication([])
    attr_editor = Editor()
    attr_editor.view.show()

    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)

    attr_editor.set_editor_options(test_data)
