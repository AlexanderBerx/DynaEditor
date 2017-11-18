from dynaeditor import const
from dynaeditor.attribute_widgets.bool_widget import BoolWidget
from dynaeditor.attribute_widgets.enum_widget import EnumWidget
from dynaeditor.attribute_widgets.float3_widget import Float3Widget
from dynaeditor.attribute_widgets.float3_color_widget import Float3ColorWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value=True, min_=None, max_=None):
        data_type = ""
        # store arguments for widget creation
        self._nice_name = nice_name
        self._default_value = default_value
        self.visible = True
        super(BoolAttribute, self).__init__(data_type, attr)

    def _create_widget(self):
        return BoolWidget(self.data_type, self.name, self._default_value, self._nice_name)


class EnumAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value, options, min_=None, max_=None):
        data_type = ""
        self._nice_name = nice_name
        self._default_value = default_value
        self._options = options
        super(EnumAttribute, self).__init__(data_type, attr)

    def _create_widget(self):
        return EnumWidget(self.data_type, self.name, self._default_value, self._options, self._nice_name)


class Float3Attribute(BaseAttribute):
    DEFAULT_MIN = [0, 0, 0]
    DEFAULT_MAX = [100, 100, 100]

    def __init__(self, attr, nice_name, default_value, color=False, min_=None, max_=None):
        type_ = const.ATYPE_FLOAT3

        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        self._nice_name = nice_name
        self._default_value = default_value
        self._color = color

        super(Float3Attribute, self).__init__(type_, attr)

    def _create_widget(self):
        if self._color:
            return Float3ColorWidget(self.data_type, self.name, self._default_value, self._nice_name)
        else:
            return Float3Widget(self.data_type, self.name, self._default_value, self._min, self._max, self._nice_name)
