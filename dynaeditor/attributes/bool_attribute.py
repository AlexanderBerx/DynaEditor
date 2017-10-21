from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attribute_name, default_value):
        widget = BoolWidget(attribute_name, default_value)
        super(BoolAttribute, self).__init__(widget, attribute_name)
