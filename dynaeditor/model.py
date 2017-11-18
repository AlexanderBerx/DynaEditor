from maya import cmds
from PySide2 import QtCore
from dynaeditor import attr_query
from dynaeditor.attributes.attribute import Attribute
from dynaeditor.prefs_manager import PrefsManager


class EditorProxyModel(QtCore.QSortFilterProxyModel):
    """
    EditorProxyModel class, inherits from QtCore.QSortFilterProxyModel,
    filters out non visible items based on the DISPLAY_ROLE of the item,
    the CheckStateRole and DisplayRole of the items are being ignored
    """
    def __init__(self):
        super(EditorProxyModel, self).__init__()
        self.setDynamicSortFilter(True)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
        overwritten method from QtCore.QSortFilterProxyModel,
        returns the data for the desired role of the given index,
        the CheckStateRole and DisplayRole of the items are being ignored
        and return None when queried
        :param index: QIndex
        :param int role: id of the role
        :return: object
        """
        if role == QtCore.Qt.CheckStateRole:
            return None
        elif role == QtCore.Qt.DisplayRole:
            return None
        return super(EditorProxyModel, self).data(index, role)

    def filterAcceptsRow(self, source_row, source_parent):
        """
        filters the given row, filters first based on the visibility of the item,
        next on all other filters
        :param source_row:
        :param source_parent:
        :return: object
        """
        source_index = self.sourceModel().index(source_row)
        if self.sourceModel().data(source_index, EditorModel.DISPLAY_ROLE) == False:
            return False

        return super(EditorProxyModel, self).filterAcceptsRow(source_row, source_parent)


class EditorModel(QtCore.QAbstractListModel):
    """
    EditorModel class, inherits from QtCore.QAbstractListModel
    """
    signal_type_changed = QtCore.Signal(str)
    WIDGET_ROLE = 20
    DISPLAY_ROLE = 21

    def __init__(self):
        super(EditorModel, self).__init__()
        self._prefs_manager = PrefsManager()
        self._node_type = None
        self._restrict_to_type = True
        self._affect_children = True
        self._items = []
        self.load_prefs()

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
        # store the visibility preferences before clearing, so if the new node has similar attributes
        # they as well would be hidden
        self.clear()
        self.add_from_mappings(attr_query.iter_obj_attrs_mapped(node))

    def add_from_mappings(self, attr_mappings, mapped=True):
        attribute_list = []
        for mapping in attr_mappings:
            try:
                if mapped:
                    attribute = Attribute(**mapping)
                else:
                    attribute = Attribute(*mapping)
            # skip not implemented types
            except TypeError:
                continue

            attribute_list.append(attribute)

        self._set_prefs_on_attribute_list(attribute_list)
        self.add_items(attribute_list)

    def _set_prefs_on_attribute_list(self, attribute_list):
        vis_prefs = self._prefs_manager.item_visibility_prefs
        for pref, setting in vis_prefs:
            if pref in attribute_list:
                attribute_list[attribute_list.index(pref)].visible = setting

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

    def load_prefs(self):
        print("need to implement prefs loading")

    def save_prefs(self):
        # save the item visibility prefs
        prefs_mapping = [(str(item), item.visible) for item in self._items]
        self._prefs_manager.item_visibility_prefs = prefs_mapping
        print("need to save other prefs to")