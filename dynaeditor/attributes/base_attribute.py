try:
    from PySide2 import QtCore
except ImportError:
    from Qt import QtCore
from dynaeditor.widgets.base_widget import BaseWidget


class BaseAttribute(QtCore.QObject):
    """
    BaseAttribute, abstract class where all attribute classes need to inherit from
    """
    _type = None
    _widget = None
    _name = None
    _visible = True
    signal_apply_attr = QtCore.Signal(str, str, str)

    def __init__(self, _type, attr):
        super(BaseAttribute, self).__init__()
        self.type_ = _type
        self.name = attr

        # ensure abstraction
        if type(self) == BaseAttribute:
            raise NotImplementedError('BaseAttribute is an abstract class')

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
        """
        :return: BaseWidget
        """
        if not self._widget:
            self._widget = self._create_widget()
            self.connect_signals()
            
        return self._widget

    def _create_widget(self):
        raise NotImplementedError()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = bool(value)

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

    @staticmethod
    def validate_args():
        raise NotImplementedError
