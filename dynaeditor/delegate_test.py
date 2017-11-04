import sys
import json
from PySide2 import QtWidgets, QtCore, QtGui
from dynaeditor.utils import general_utils
from dynaeditor.attributes.attribute import Attribute


class AttrDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, *args, **kwargs):
        super(AttrDelegate, self).__init__(*args, **kwargs)

    def createEditor(self, parent, option, index):
        print("Getting delegate editor")
        editor = QtWidgets.QComboBox(parent)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        print value

    def setModelData(self, editor, model, index):
        return

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def paint(self, painter, option, index):
        QtWidgets.QApplication.style().drawControl(Q.QStyle.CE_CheckBox, check_box_style_option, painter)


class AttrModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(AttrModel, self).__init__(*args, **kwargs)
        self.__attr_items = []

    def set_attrs(self, attrs):
        self.__attr_items = attrs

    def rowCount(self, parent):
        return len(self.__attr_items)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.__attr_items[index.row()]

    def setData(self, index, value, role):
        self.__attr_items[index.row()] = value
        return True

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable


class AttrView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super(AttrView, self).__init__(*args, **kwargs)


def main():
    app = QtWidgets.QApplication(sys.argv)
    view = AttrView()

    model = AttrModel()
    model.set_attrs(["test" for i in range(5)])
    view.setModel(model)

    delegate = AttrDelegate()
    view.setItemDelegate(delegate)

    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
