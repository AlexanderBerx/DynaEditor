try:
    from PySide2 import QtCore, QtWidgets, QtGui
except ImportError:
    from Qt import QtCore


class BaseAttribute(object):
    """
    BaseAttribute, abstract class where all attribute classes need to inherit from
    """
    _type = None
    _name = None
    _visible = True

    def __init__(self, _type, attr):
        self.type_ = _type
        self.name = attr

        # ensure abstraction
        if type(self) == BaseAttribute:
            raise NotImplementedError('BaseAttribute is an abstract class')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

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
