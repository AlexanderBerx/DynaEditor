from dynaeditor import const
from dynaeditor.widgets.float3_widget import Float3Widget
from dynaeditor.attributes.base_attribute import BaseAttribute


class Float3Attribute(BaseAttribute):
    def __init__(self, attr, default_value, nice_name, _min=None, _max=None):
        if not _min:
            _min = [0, 0, 0]
        if not _max:
            _max = [100, 100, 100]

        _type = const.ATYPE_BOOL
        widget = Float3Widget(nice_name, default_value, _min, _max)
        super(Float3Attribute, self).__init__(_type, widget, attr)
