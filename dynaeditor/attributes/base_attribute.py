class BaseAttribute(object):
    """
    BaseAttribute, abstract class where all attribute classes need to inherit from
    """
    _data_type = None
    _name = None
    _visible = True
    _nice_name = None
    _default_value = None

    def __init__(self, attr, nice_name, default_value, type_=''):
        self.data_type = type_
        self.name = attr
        self.nice_name = nice_name
        self.default_value = default_value

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self._name == other

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

    @property
    def nice_name(self):
        return self._nice_name

    @nice_name.setter
    def nice_name(self, value):
        self._nice_name = value

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
