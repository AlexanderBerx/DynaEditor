

class BaseAttribute(object):
    def __init__(self, widget):
        self._widget = widget

    @property
    def widget(self):
        if not self._widget:
            raise NotImplementedError("No Widget Assigned")
        return self._widget

    @widget.setter
    def widget(self, value):
        self._widget = value
