from PySide2 import QtCore
from dynaeditor.attributes.attribute import Attribute


class DisplayModelDelegate(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    def __init__(self, parent=None):
        super(DisplayModelDelegate, self).__init__(parent)
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
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable

    def rowsAboutToBeInserted(self, parent, first, last):
        super(DisplayModelDelegate, self).rowsAboutToBeInserted(parent, first, last)

    def emit_update(self):
        self.rowsInserted.emit(None, 0, self.rowCount())

class EditorModel(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    VISIBILITY_ROLE = 21
    signal_apply_attr = QtCore.Signal(str, str, str)
    _display_delegate = None

    def __init__(self):
        super(EditorModel, self).__init__()
        self._items = []

    def get_model_delegate(self):
        if not self._display_delegate:
            self._display_delegate = DisplayModelDelegate()
            self._display_delegate.set_parent_model(self)
            # connect signals from parent to child
        return self._display_delegate

    def _update_delegate(self):
        if not self._display_delegate:
            return
        self._display_delegate.emit_update()

    def set_to_node(self, node):
        self.clear()

    def add_from_mappings(self, attr_mappings):
        for mapping in attr_mappings:
            try:
                attribute = Attribute(**mapping)
            # skip not implemented types
            except TypeError as e:
                continue
            attribute.setCheckable(True)
            attribute.flags()
            self.add_item(attribute)
        self._update_delegate()

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
            # self._update_delegate()
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
