import json
from PySide2 import QtCore, QtWidgets
from dynaeditor.utils import general_utils
from dynaeditor.attributes.attribute import Attribute


class EditorModel(QtCore.QAbstractListModel):
    def __init__(self):
        super(EditorModel, self).__init__()
        self._attr_items = []

    def attrs_from_mapping(self, attr_mappings):
        for mapping in attr_mappings:
            try:
                attribute = Attribute(**mapping)
            except TypeError:
                continue
            self._attr_items.append(attribute)

    def rowCount(self, parent):
        return len(self._attr_items)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._attr_items[index.row()].widget
        elif role == QtCore.Qt.SizeHintRole:
            return self._attr_items[index.row()].widget.sizeHint()
        else:
            pass


class ListView(QtWidgets.QListView):
    def __init__(self):
        super(ListView, self).__init__()

    def setIndexWidget(self, *args, **kwargs):
        print("setting widget")
        super(ListView, self).setIndexWidget(*args, **kwargs)

    def setItemDelegateForRow(self, *args, **kwargs):
        print("setting delegate")
        super(ListView, self).setItemDelegateForRow(*args, **kwargs)


def load_test_data(model):
    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(data) for data in test_data]

    model.attrs_from_mapping(mapped_data)


def main():
    app = QtWidgets.QApplication([])
    model = EditorModel()
    load_test_data(model)
    view = ListView()
    view.show()
    view.setModel(model)
    app.exec_()

if __name__ == '__main__':
    main()
