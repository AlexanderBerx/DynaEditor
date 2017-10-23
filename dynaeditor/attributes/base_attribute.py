from PySide2 import QtCore

class BaseAttribute(QtCore.QObject):
    signal_apply_attr = QtCore.Signal(str)

    def __init__(self, widget, attr):
        super(BaseAttribute, self).__init__()
        self.widget = widget
        self.name = attr

    @property
    def widget(self):
        if not self._widget:
            raise NotImplementedError("No Widget Assigned")
        return self._widget

    @widget.setter
    def widget(self, value):
        self._widget = value

    @property
    def name(self):
        if not self._name:
            raise NotImplementedError("No Name has been set")
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
