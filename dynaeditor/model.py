from PySide2 import QtCore
from dynaeditor.attributes.attribute import Attribute


class EditorModel(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20

    def __init__(self):
        super(EditorModel, self).__init__()
        self._items = []

    def add_from_mappings(self, attr_mappings):
        for mapping in attr_mappings:
            try:
                attribute = Attribute(**mapping)
            # skip not implemented types
            except TypeError as e:
                continue
            self.add_item(attribute)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == self.WIDGET_ROLE:
            return self._items[index.row()].widget
        elif role == QtCore.Qt.DisplayRole:
            return self._items[index.row()]
        return None

    def add_item(self, item):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._items), len(self._items))
        self._items.append(item)
        self.endInsertRows()

    def add_items(self, item_list):
        for item in item_list:
            self.add_item(item)

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        if row < 0 or row > len(self._items):
            return

        self.beginRemoveRows(parent, row, row + count - 1)
        while count != 0:
            del self._items[row]
            count -= 1

        self.endRemoveRows()

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable
