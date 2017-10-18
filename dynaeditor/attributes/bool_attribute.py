from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self):
        widget = BoolWidget()
        super(BoolAttribute, self).__init__()
