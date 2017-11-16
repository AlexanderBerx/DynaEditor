from PySide2 import QtCore, QtGui
from dynaeditor.attributes.attribute import Attribute


class EditorProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super(EditorProxyModel, self).__init__()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.CheckStateRole:
            return None
        if role == QtCore.Qt.DisplayRole:
            return None
        else:
            return super(EditorProxyModel, self).data(index, role)

    def filterAcceptsRow(self, source_row, source_parent):
        source_index = self.sourceModel().index(source_row)
        return self.sourceModel().data(source_index, EditorModel.DISPLAY_ROLE)


class EditorModel(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    DISPLAY_ROLE = 21

    def __init__(self):
        super(EditorModel, self).__init__()
        self._items = []

    def set_to_node(self, node):
        self.clear()

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

    def row_count_visible(self):
        return len(self.get_visible())

    def get_visible(self):
        return [i for i in self._items if i.visible == True]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == self.WIDGET_ROLE:
            return self._items[index.row()].widget
        elif role == self.DISPLAY_ROLE:
            return self._items[index.row()].visible
        elif role == QtCore.Qt.CheckStateRole:
            return self._items[index.row()].visible
        elif role == QtCore.Qt.StatusTipRole:
            return str(self._items[index.row()])
        elif role == QtCore.Qt.WhatsThisRole:
            return str(self._items[index.row()])

        #elif role == QtCore.Qt.SizeHintRole:
        #    if self._items[index.row()].widget:
        #        return self._items[index.row()].widget.sizeHint()

        elif role == QtCore.Qt.DisplayRole:
            return str(self._items[index.row()])
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.CheckStateRole:
            self._items[index.row()].visible = not self._items[index.row()].visible
            self.dataChanged.emit(index, index, 1)
            return True
        return False

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

    def clear(self):
        self.removeRows(0, self.rowCount())

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
