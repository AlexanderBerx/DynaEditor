from dynaeditor import const
from dynaeditor.widgets.float3_widget import Float3Widget
from dynaeditor.widgets.float3_color_widget import Float3ColorWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class Float3Attribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value, color=False, _min=None, _max=None, categories=None):
        if not _min:
            _min = [0, 0, 0]
        if not _max:
            _max = [100, 100, 100]

        _type = const.ATYPE_FLOAT3
        if color:
            widget = Float3ColorWidget(nice_name, default_value)
        else:
            widget = Float3Widget(nice_name, default_value, _min, _max)
        super(Float3Attribute, self).__init__(_type, widget, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, color=None, _min=None, _max=None, categories=None):
        if not attr or not nice_name or not default_value:
            return False
        return True
