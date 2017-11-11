import sys
from PySide2 import QtWidgets, QtCore


class AttrModel(QtCore.QAbstractListModel):
    WIDGET_ROLE = 20
    def __init__(self, *args, **kwargs):
        super(AttrModel, self).__init__(*args, **kwargs)
        self._items = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._items)


    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == self.WIDGET_ROLE:
            return QtWidgets.QComboBox()
        elif role == QtCore.Qt.DisplayRole:
            return self._items[index.row()]
        return None

    """
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self._items[index.row()] = value
            # self.dataChanged.emit(index, index)
        return True
    """

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


class AttrView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super(AttrView, self).__init__(*args, **kwargs)
        self.setAlternatingRowColors(True)

    def _set_items_widget(self, start=None, end=None):
        model = self.model()
        if not model:
            return

        if not start:
            start = 0
        if not end:
            end = self.model().rowCount()
        items = range(start, end)


        for index in items:
            # get the index to the model
            index = model.index(index)
            # if the item has already an widget assigned to it, skip it
            if self.indexWidget(index):
                continue
            widget = model.data(index, AttrModel.WIDGET_ROLE)
            self.setIndexWidget(index, widget)

    def setModel(self, model):
        super(AttrView, self).setModel(model)
        self._set_items_widget()

    def update(self, index):
        print("update")
        super(AttrView, self).update(index)

    def edit(self, index):
        print("edit")
        super(AttrView, self).edit(index)

    def rowsInserted(self, parent, start, end):
        super(AttrView, self).rowsInserted(parent, start, end)

        # make sure new items also have there widget
        if start == end:
            end += 1
        self._set_items_widget(start, end)

def main():
    app = QtWidgets.QApplication(sys.argv)
    view = AttrView()

    model = AttrModel()
    model.add_items(["test" for i in range(5)])
    view.setModel(model)

    view.show()
    model.add_items(["test" for i in range(5)])
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
