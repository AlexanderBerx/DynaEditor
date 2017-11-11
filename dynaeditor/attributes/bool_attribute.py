from dynaeditor import const
from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value=True, _min=0, _max=1, categories=None):
        _type = const.ATYPE_BOOL
        # store arguments for widget creation
        self._nice_name = nice_name
        self._default_value = default_value
        super(BoolAttribute, self).__init__(_type, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, _min=None, _max=None, categories=None):
        if not attr or not nice_name:
            return False
        return True

    def _create_widget(self):
        return BoolWidget(self._nice_name, self._default_value)
