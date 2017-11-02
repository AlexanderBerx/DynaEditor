import json
from PySide2 import QtCore
from dynaeditor.utils import general_utils
from dynaeditor.attributes.attribute import Attribute


class EditorModel(QtCore.QAbstractListModel):
    def __init__(self):
        super(EditorModel, self).__init__()
        self._attr_items = []

    def attrs_from_mapping(self, attr_mappings):
        for mapping in attr_mappings:
            print mapping
            attribute = Attribute(**mapping)
            #self._attr_items.append(attribute)


def load_test_data(model):
    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(data) for data in test_data]

    model.attrs_from_mapping(mapped_data)

def main():
    model = EditorModel()
    load_test_data(model)

if __name__ == '__main__':
    main()
