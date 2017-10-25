from PySide2 import QtCore
from dynaeditor.widgets.base_widget import BaseWidget


class BaseAttribute(QtCore.QObject):
    _type = None
    _widget = None
    _name = None
    signal_apply_attr = QtCore.Signal(str, str, str)

    def __init__(self, _type, widget, attr):
        super(BaseAttribute, self).__init__()
        self.type_ = _type
        self.widget = widget  # type:BaseWidget
        self.name = attr
        self.connect_signals()

    @property
    def type_(self):
        if not self._type:
            raise NotImplementedError("No type set")
        return self._type

    @type_.setter
    def type_(self, value):
        self._type = value

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

    def connect_signals(self):
        self.widget.signal_apply_attr[str].connect(self._emit_attr)

    @QtCore.Slot(str)
    def _emit_attr(self, value):
        self.signal_apply_attr.emit(self.name, self.type_, value)
