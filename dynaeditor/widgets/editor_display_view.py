from PySide2 import QtWidgets


class EditorDisplayView(QtWidgets.QListView):
    def __init__(self):
        super(EditorDisplayView, self).__init__()

    def _update_items(self):
        pass

    def setModel(self, model):
        super(EditorDisplayView, self).setModel(model)

    def rowsInserted(self, parent, start, end):
        super(EditorDisplayView, self).rowsInserted(parent, start, end)
        print("inserting")