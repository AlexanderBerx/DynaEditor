

class BaseAttribute(object):
    def __init__(self, widget, attr):
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
