# -*- coding: utf-8 -*-
# Written by Robin Burchell
# No licence specified or required, but please give credit where it's due,
# and please let me know if this helped you. Feel free to contact with corrections or suggestions.
#
# We're using PySide, Nokia's official LGPL bindings.
# You can however easily use PyQt (Riverside Computing's GPL bindings) by
# commenting these and fixing the appropriate imports.
from PySide.QtCore import *
from PySide.QtGui import *
# from PyQt4 import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
import sys


# This is our model. It will maintain, modify, and present data to our view(s).
# For more information on list models, take a look at:
# http://doc.trolltech.com/4.6/qabstractitemmodel.html
class SimpleListModel(QAbstractListModel):
    def __init__(self, mlist):
        QAbstractListModel.__init__(self)

        # Store the passed data list as a class member.
        self._items = mlist

    # We need to tell the view how many rows we have present in our data. see tutorial #3
    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    # view is asking us about some of our data.
    # see tutorial #3 for more information on this.
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return QVariant(self._items[index.row()])
        elif role == Qt.EditRole:
            # The view is asking for the editable form of the data. i.e. unformatted.
            # See the comment in setData().
            return QVariant(self._items[index.row()])
        else:
            return QVariant()

    # the view is asking us to *change* some aspect of our data.
    # as in the above, it can be any aspect of the data, not *just* the information contained in the model.
    # remember to return true if you handle a data change, and false otherwise, always!
    # for more information, see:
    # http://doc.trolltech.com/4.6/qabstractitemmodel.html#setData
    def setData(self, index, value, role=Qt.EditRole):
        # You might be expecting Qt.DisplayRole here, but no.
        # Qt.DisplayRole is the *displayed* value of an item, like, a formatted currency value: "$44.00"
        # Qt.EditRole is the raw data of an item, e.g. "4400" (as in cents).
        if role == Qt.EditRole:
            # set the data.
            # the str() cast here is mostly for peace of mind, you can't perform some operations
            # in python with Qt types, like pickling.
            self._items[index.row()] = str(value.toString().toUtf8())

            # *always* emit the dataChanged() signal after changing any data inside the model.
            # this is so e.g. the different views know they need to do things with it.
            #
            # don't be lazy and pass a huge range of values to this, because it is processing-heavy.
            #
            # because we are a simple list, we only have one index to worry about for topleft/bottom right,
            # so just reuse the index we are passed.
            QObject.emit(self, SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            return True
        # unhandled change.
        return False

    # if you e.g. don't want to make an item selectable, or draggable, here's the place to do it.
    # by default, items are enabled, and selectable, but we want to make them editable too, so we need to
    # reimplement this. of course, this means you can make only specific items selectable, for example,
    # by using the 'index' parameter.
    # For more information, see:
    # http://doc.trolltech.com/4.6/qabstractitemmodel.html#flags
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled

    # remove rows from our model.
    # 'row' is the row number to be removed, 'count' are the total number of rows to remove.
    # 'parent' is the 'parent' of the initial row: this is pretty much only relevant for tree models etc.
    # For more information, see:
    # http://doc.trolltech.com/4.6/qabstractitemmodel.html#removeRows
    def removeRows(self, row, count, parent=QModelIndex()):
        # make sure the index is valid, to avoid IndexErrors ;)
        if row < 0 or row > len(self._items):
            return

        # let the model know we're changing things.
        # we may have to remove multiple rows, if not, this could be handled simpler.
        self.beginRemoveRows(parent, row, row + count - 1)

        # actually remove the items from our internal data representation
        while count != 0:
            del self._items[row]
            count -= 1

        # let the model know we're done
        self.endRemoveRows()

    # while we could use QAbstractItemModel::insertRows(), we'd have to shoehorn around the API
    # to get things done: we'd need to call setData() etc.
    # The easier way, in this case, is to use our own method to do the heavy lifting.
    def addItem(self, item):
        # The str() cast is because we don't want to be storing a Qt type in here.
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items))
        self._items.append(str(item))
        self.endInsertRows()


# This widget is our view of the readonly list.
# For more information, see:
# http://doc.trolltech.com/4.6/qlistview.html
class SimpleListView(QListView):
    def __init__(self, parent=None):
        QListView.__init__(self, parent)

        # unlike the previous tutorial, we'll do background colours 'properly'. ;)
        self.setAlternatingRowColors(True)

        # we want our listview to have a context menu taken from the actions on this widget
        # those actions will be to delete an item :)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

        # create a menu item for our context menu that will delete the selected item.
        a = QAction("Delete Selected", self)

        # hook up the triggered() signal on the menu item to the slot below.
        QObject.connect(a, SIGNAL("triggered()"), self, SLOT("onTriggered()"))
        self.addAction(a)

    # this is a slot! we covered signals and slots in tutorial #2,
    # but this is the first time we've created one ourselves.
    @pyqtSlot()
    def onTriggered(self):
        # tell our model to remove the selected row.
        self.model().removeRows(self.currentIndex().row(), 1)


# Our main application window.
# You should be used to this from previous tutorials.
class MyMainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        # main section of the window
        vbox = QVBoxLayout()

        # create a data source:
        self._model = SimpleListModel(["test", "tes1t", "t3est", "t5est", "t3est"])

        # let's add two views of the same data source we just created:
        v = SimpleListView()
        v.setModel(self._model)
        vbox.addWidget(v)

        # second view..
        v = SimpleListView()
        v.setModel(self._model)
        vbox.addWidget(v)

        # bottom section of the window:
        # let's have a text input and a pushbutton that add an item to our model.
        hbox = QHBoxLayout()
        self._itemedit = QLineEdit()

        # create the button, and hook it up to the slot below.
        b = QPushButton("Add Item")
        QObject.connect(b, SIGNAL("clicked()"), self, SLOT("doAddItem()"))

        hbox.addWidget(self._itemedit)
        hbox.addWidget(b)

        # add bottom to main window layout
        vbox.addLayout(hbox)

        # set layout on the window
        self.setLayout(vbox)

    @pyqtSlot()
    def doAddItem(self):
        # instruct the model to add an item
        self._model.addItem(self._itemedit.text())

        # blank the text input.
        self._itemedit.setText("")


# set things up, and run it. :)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
    sys.exit()