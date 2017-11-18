from PySide2 import QtWidgets, QtCore
from dynaeditor.model import EditorModel


class EditorView(QtWidgets.QListView):
    """
    EditorView class, inherits from QtWidgets.QListView,
    view class that sets item widgets based on the data of the attached model,
    widgets are being set implicitly when a model is being set or when rows
    are inserted. Emits signal_apply_attr when one of the item widgets are being
    clicked.
    """
    signal_apply_attr = QtCore.Signal(str, str, str)
    def __init__(self):
        super(EditorView, self).__init__()
        self.setAlternatingRowColors(True)

    def set_items_widget(self, start=None, end=None):
        """
        sets the widgets of the items, if no start or end is given
        widgets are being set to all the items available
        :param int start: start index
        :param int end: end index
        :return: None
        """
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
            index = model.index(index, 0)
            # if the item has already an widget assigned to it, skip it
            if self.indexWidget(index):
                continue
            widget = model.data(index, EditorModel.WIDGET_ROLE)
            widget.signal_apply_attr[str, str, str].connect(self._emit_apply_attr)
            self.setIndexWidget(index, widget)

    def setModel(self, model):
        """
        sets the model of the view and sets the widgets of all the items
        :param model:
        :return: None
        """
        super(EditorView, self).setModel(model)
        self.set_items_widget()

    def rowsInserted(self, parent, start, end):
        """
        inserts the rows according the given parameters, and sets the widgets of the
        inserted rows
        :param parent:
        :param start:
        :param end:
        :return: None
        """
        super(EditorView, self).rowsInserted(parent, start, end)
        # make sure new items also have there widget
        if start == end:
            end += 1
        self.set_items_widget(start, end)

    @QtCore.Slot(str, str, str)
    def _emit_apply_attr(self, attr_name, attr_value, attr_type):
        """
        slot for connecting item widgets attribute signals to
        :param attr_name:
        :param attr_value:
        :param attr_type:
        :return:
        """
        self.signal_apply_attr.emit(attr_name, attr_value, attr_type)
