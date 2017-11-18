try:
    from PySide2 import QtCore, QtWidgets, QtGui
except ImportError:
    from Qt import QtCore


class BaseAttribute(object):
    """
    BaseAttribute, abstract class where all attribute classes need to inherit from
    """
    _data_type = None
    _name = None
    _visible = True

    def __init__(self, _type, attr):
        self.data_type = _type
        self.name = attr

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value

    @property
    def widget(self):
        """
        :return: BaseWidget
        """
        return self._create_widget()

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
