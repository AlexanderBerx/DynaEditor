from dynaeditor import const
from dynaeditor.widgets.enum_widget import EnumWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class EnumAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value, options, _min=None, _max=None, categories=None):
        _type = const.ATYPE_ENUM
        widget = EnumWidget(nice_name, default_value, options)
        super(EnumAttribute, self).__init__(_type, widget, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, options=None, _min=None,
                      _max=None, categories=None):
        if not attr or not nice_name or not default_value or not options:
            return False
        return True
