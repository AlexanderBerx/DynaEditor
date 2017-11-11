from PySide2 import QtWidgets, QtCore
from dynaeditor.model import EditorModel


class EditorView(QtWidgets.QListView):

    def __init__(self):
        super(EditorView, self).__init__()
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
            widget = model.data(index, EditorModel.WIDGET_ROLE)
            self.setIndexWidget(index, widget)

    def setModel(self, model):
        super(EditorView, self).setModel(model)
        self._set_items_widget()

    def rowsInserted(self, parent, start, end):
        super(EditorView, self).rowsInserted(parent, start, end)

        # make sure new items also have there widget
        if start == end:
            end += 1
        self._set_items_widget(start, end)
