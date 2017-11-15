from PySide2 import QtCore
from dynaeditor.attributes.attribute import Attribute


class ModelProxy(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    def __init__(self, parent=None):
        super(ModelProxy, self).__init__(parent)
        self._items = []
        self._parent_model = None #  type:EditorModel

    def set_parent_model(self, model):
        self._parent_model = model

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self._parent_model.row_count_visible()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        visible = self._parent_model.get_visible()
        if role == self.WIDGET_ROLE:
            widget = visible[index.row()].widget
            # connect the signal
            # visible[index.row()].signal_apply_attr[str, str, str].connect(self.apply_attr)
            return widget
        elif role == QtCore.Qt.StatusTipRole:
            return str(visible[index.row()])
        elif role == QtCore.Qt.WhatsThisRole:
            return str(visible[index.row()])
        elif role == QtCore.Qt.SizeHintRole:
            return visible[index.row()].widget.sizeHint()
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class EditorModel(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    VISIBILITY_ROLE = 21
    signal_apply_attr = QtCore.Signal(str, str, str)
    _proxy = None

    def __init__(self):
        super(EditorModel, self).__init__()
        self._items = []

    def get_model_proxy(self):
        if not self._proxy:
            self._proxy = ModelProxy()
            self._proxy.set_parent_model(self)
            # connect signals from current to the delegate

        return self._proxy

    def _update_proxy(self, index=None):
        # if no index is being passed on updated the whole proxy
        if not index:
            self._proxy.insertRow(0)
            self._proxy.beginInsertRows(self._proxy.index(0), 0, self.row_count_visible())
            self._proxy.endInsertRows()
            return

        item = self._items[index.row()]
        # update the proxy based on the visibility value of the item
        if item.visible == True:
            # note: an item being made visible translates as an row adding in the proxy model
            print("show")
            item_index = self.get_visible().index(item)
            print item_index
            self._proxy.insertRow(item_index+1)
            self._proxy.beginInsertRows(self._proxy.index(item_index), item_index, item_index + 1)
            #self._proxy.endInsertRows()

        else:
            # note: an item being hidden translates as an row being removed in the proxy model

            # item_index = self.get_visible().index(item)
            # self._proxy.rowsAboutToBeRemoved.emit(None, item_index, item_index)
            print("hidden")

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
        self._update_proxy()

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._items)

    def row_count_visible(self):
        return len(self.get_visible())

    def get_visible(self):
        return [i for i in self._items if i.visible == True]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == self.WIDGET_ROLE:
            widget = self._items[index.row()].widget
            # connect the signal
            self._items[index.row()].signal_apply_attr[str, str, str].connect(self.apply_attr)
            return widget
        elif role == QtCore.Qt.CheckStateRole:
            return self._items[index.row()].visible
        elif role == self.VISIBILITY_ROLE:
            return self._items[index.row()].visible
        elif role == QtCore.Qt.StatusTipRole:
            return str(self._items[index.row()])
        elif role == QtCore.Qt.WhatsThisRole:
            return str(self._items[index.row()])
        elif role == QtCore.Qt.SizeHintRole:
            return self._items[index.row()].widget.sizeHint()
        elif role == QtCore.Qt.DisplayRole:
            return str(self._items[index.row()])
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.CheckStateRole:
            self._items[index.row()].visible = not self._items[index.row()].visible
            self._update_proxy(index)
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

    @QtCore.Slot(str, str, str)
    def apply_attr(self, name, type_, value):
        self.signal_apply_attr.emit(name, type_, value)
