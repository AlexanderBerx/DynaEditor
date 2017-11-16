from dynaeditor import const
from dynaeditor.widgets.bool_widget import BoolWidget
from dynaeditor.widgets.enum_widget import EnumWidget
from dynaeditor.widgets.float3_widget import Float3Widget
from dynaeditor.widgets.float3_color_widget import Float3ColorWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value=True, _min=0, _max=1, categories=None):
        type_ = const.ATYPE_BOOL
        # store arguments for widget creation
        self._nice_name = nice_name
        self._default_value = default_value
        self.visible = True
        super(BoolAttribute, self).__init__(type_, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, min_=None, max_=None, categories=None):
        if not attr or not nice_name:
            return False
        return True

    def _create_widget(self):
        return BoolWidget(self.type_, self.name, self._default_value, self._nice_name)


class EnumAttribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value, options, min_=None, max_=None, categories=None):
        type_ = const.ATYPE_ENUM
        self._nice_name = nice_name
        self._default_value = default_value
        self._options = options
        super(EnumAttribute, self).__init__(type_, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, options=None, min_=None,
                      max_=None, categories=None):
        if not attr or not nice_name or not default_value or not options:
            return False
        return True

    def _create_widget(self):
        return EnumWidget(self.type_, self.name, self._default_value, self._options, self._nice_name)


class Float3Attribute(BaseAttribute):
    def __init__(self, attr, nice_name, default_value, color=False, min_=None, max_=None, categories=None):
        type_ = const.ATYPE_FLOAT3

        if not min_:
            self._min = [0, 0, 0]
        else:
            self._min = min_
        if not max_:
            self._max = [100, 100, 100]
        else:
            self._max = max_
        self._nice_name = nice_name
        self._default_value = default_value
        self._color = color

        super(Float3Attribute, self).__init__(type_, attr)

    @staticmethod
    def validate_args(attr=None, nice_name=None, default_value=None, color=None, min_=None, max_=None, categories=None):
        if not attr or not nice_name or not default_value:
            return False
        return True

    def _create_widget(self):
        if self._color:
            return Float3ColorWidget(self.type_, self.name, self._default_value, self._nice_name)
        else:
            return Float3Widget(self.type_, self.name, self._default_value, self._min, self._max, self._nice_name)
