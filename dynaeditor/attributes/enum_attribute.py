from dynaeditor import const
from dynaeditor.widgets.enum_widget import EnumWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class EnumAttribute(BaseAttribute):
    def __init__(self, attr, default_value, nice_name, options, _min=None, _max=None):
        _type = const.ATYPE_ENUM
        widget = EnumWidget(nice_name, default_value, options)
        super(EnumAttribute, self).__init__(_type, widget, attr)
