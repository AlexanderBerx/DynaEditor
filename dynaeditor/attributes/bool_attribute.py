from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attr, default_value, nice_name, _min=0, _max=1):
        widget = BoolWidget(nice_name, default_value)
        super(BoolAttribute, self).__init__(widget, attr)
