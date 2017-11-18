from maya import cmds
from PySide2 import QtCore
from dynaeditor import attr_query
from dynaeditor.attributes.attribute import Attribute


class EditorProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super(EditorProxyModel, self).__init__()
        self.setDynamicSortFilter(True)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.CheckStateRole:
            return None
        if role == QtCore.Qt.DisplayRole:
            return None
        else:
            return super(EditorProxyModel, self).data(index, role)

    def filterAcceptsRow(self, source_row, source_parent):
        source_index = self.sourceModel().index(source_row)
        if self.sourceModel().data(source_index, EditorModel.DISPLAY_ROLE) == False:
            return False

        return super(EditorProxyModel, self).filterAcceptsRow(source_row, source_parent)


class EditorModel(QtCore.QAbstractListModel):
    signal_type_changed = QtCore.Signal(str)
    WIDGET_ROLE = 20
    DISPLAY_ROLE = 21

    def __init__(self):
        super(EditorModel, self).__init__()
        self._node_type = None
        self._restrict_to_type = True
        self._affect_children = True
        self._items = []

    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
        self.signal_type_changed.emit(value)

    @property
    def restrict_to_type(self):
        return self._restrict_to_type

    @restrict_to_type.setter
    def restrict_to_type(self, value):
        self._restrict_to_type = bool(value)

    @property
    def affect_children(self):
        return self._affect_children

    @affect_children.setter
    def affect_children(self, value):
        self._affect_children = bool(value)

    def set_to_node(self, node):
        node_type = cmds.objectType(node)
        if node_type == self.node_type:
            return
        self.node_type = node_type
        self.clear()
        self.add_from_mappings(attr_query.iter_obj_attrs_mapped(node))

    def add_from_mappings(self, attr_mappings, mapped=True):
        for mapping in attr_mappings:
            try:
                if mapped:
                    attribute = Attribute(**mapping)
                else:
                    attribute = Attribute(*mapping)
            # skip not implemented types
            except TypeError:
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
        elif role == QtCore.Qt.SizeHintRole:
            # hardcoded value due to usage of widgets
            return QtCore.QSize(100, 20)
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
