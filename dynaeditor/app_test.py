import json
from PySide2 import QtWidgets
from dynaeditor.model import EditorModel
from dynaeditor.utils import general_utils
from dynaeditor.widgets.editor_view import EditorView


def main():
    app = QtWidgets.QApplication([])
    model = EditorModel()

    view = EditorView()
    view.setModel(model)
    view.show()

    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(data) for data in test_data]
    model.add_from_mappings(mapped_data)

    app.exec_()

if __name__ == '__main__':
    main()
