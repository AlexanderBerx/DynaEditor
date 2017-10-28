from dynaeditor import const
from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value=1, _min=0, _max=1):
        _type = const.ATYPE_BOOL
        widget = BoolWidget(nice_name, default_value)
        super(BoolAttribute, self).__init__(_type, widget, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, _min=None, _max=None):
        if not attr or not nice_name or not default_value:
            return False
        return True
