"""
attribute type classes all inherit from BaseAttribute
"""
from dynaeditor import const
from dynaeditor.attribute_widgets.bool_widget import BoolWidget
from dynaeditor.attribute_widgets.enum_widget import EnumWidget
from dynaeditor.attribute_widgets.float3_widget import Float3Widget
from dynaeditor.attribute_widgets.float2_widget import Float2Widget
from dynaeditor.attribute_widgets.float3_color_widget import Float3ColorWidget
from dynaeditor.attribute_widgets.float_widget import FloatWidget
from dynaeditor.attributes.base_attribute import BaseAttribute


class BoolAttribute(BaseAttribute):
    """
    BoolAttribute, inherits from BaseAttribute, for maya bool attributes
    """
    def __init__(self, attr, nice_name, default_value=True, min_=None, max_=None):
        # note: bool attributes don't need a min & max but since querying it will always
        # return it the params are there
        super(BoolAttribute, self).__init__(attr, nice_name, default_value)

    def _create_widget(self):
        return BoolWidget(self.data_type, self.name, self.default_value, self.nice_name)


class EnumAttribute(BaseAttribute):
    """
    EnumAttribute, inherits from BaseAttribute, for maya enum attributes
    """
    def __init__(self, attr, nice_name, default_value, options, min_=None, max_=None):
        self._options = options
        super(EnumAttribute, self).__init__(attr, nice_name, default_value)

    def _create_widget(self):
        return EnumWidget(self.data_type, self.name, self.default_value, self._options, self.nice_name)


class FloatAttribute(BaseAttribute):
    """
    FloatAttribute, inherits from BaseAttribute, for maya float attributes
    """
    DEFAULT_MIN = -15000.0
    DEFAULT_MAX = 15000.0

    def __init__(self, attr, nice_name, default_value, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        super(FloatAttribute, self).__init__(attr, nice_name, default_value)

    def _create_widget(self):
        return FloatWidget(self.data_type, self.name, self.default_value, self._min,
                           self._max, slider=True, nice_name=self.nice_name)


class Float2Attribute(BaseAttribute):
    """
    Float2Attribute, inherits from BaseAttribute, for maya float2 attributes
    """
    def __init__(self, attr, nice_name, default_value):
        super(Float2Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_FLOAT2)

    def _create_widget(self):
        return Float2Widget(self.data_type, self.name, self.default_value, nice_name=self.nice_name)


class Float3Attribute(BaseAttribute):
    """
    Float3Attribute, inherits from BaseAttribute, for maya float3 attributes
    """
    DEFAULT_MIN = [0.0, 0.0, 0.0]
    DEFAULT_MAX = [100.0, 100.0, 100.0]

    def __init__(self, attr, nice_name, default_value, color=False, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        self._color = color
        super(Float3Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_FLOAT3)

    def _create_widget(self):
        if self._color:
            return Float3ColorWidget(self.data_type, self.name, self.default_value, self.nice_name)
        else:
            return Float3Widget(self.data_type, self.name, self.default_value, self._min, self._max, self.nice_name)


class DoubleAttribute(BaseAttribute):
    """
    DoubleAttribute, inherits from BaseAttribute, for maya double attributes
    """
    def __init__(self, attr, nice_name, default_value):
        super(DoubleAttribute, self).__init__(attr, nice_name, default_value, const.ATYPE_DOUBLE)

    def _create_widget(self):
        return FloatWidget(self.data_type, self.name, self.default_value, slider=True, nice_name=self.nice_name)


class Double2Attribute(BaseAttribute):
    """
    Double2Attribute, inherits from BaseAttribute, for maya double2 attributes
    """
    def __init__(self, attr, nice_name, default_value):
        super(Double2Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_DOUBLE2)

    def _create_widget(self):
        return Float2Widget(self.data_type, self.name, self.default_value, nice_name=self.nice_name)


class Double3Attribute(BaseAttribute):
    """
    Double3Attribute, inherits from BaseAttribute, for maya double3 attributes
    """
    DEFAULT_MIN = [0.0, 0.0, 0.0]
    DEFAULT_MAX = [100.0, 100.0, 100.0]

    def __init__(self, attr, nice_name, default_value, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        super(Double3Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_DOUBLE3)

    def _create_widget(self):
        return Float3Widget(self.data_type, self.name, self.default_value, self._min, self._max, self.nice_name)


class LongAttribute(BaseAttribute):
    """
    LongAttribute, inherits from BaseAttribute, for maya long attributes
    """
    DEFAULT_MIN = 0.0
    DEFAULT_MAX = 100.0

    def __init__(self, attr, nice_name, default_value, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        super(LongAttribute, self).__init__(attr, nice_name, default_value)

    def _create_widget(self):
        return FloatWidget(self.data_type, self.name, self.default_value, self._min, self._max,
                           slider=True, nice_name=self.nice_name)


class Long2Attribute(BaseAttribute):
    """
    Long2Attribute, inherits from BaseAttribute, for maya long2 attributes
    """
    def __init__(self, attr, nice_name, default_value):
        super(Long2Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_LONG2)

    def _create_widget(self):
        return Float2Widget(self.data_type, self.name, self.default_value, nice_name=self.nice_name)


class Long3Attribute(BaseAttribute):
    """
    Long3Attribute, inherits from BaseAttribute, for maya long3 attributes
    """
    DEFAULT_MIN = [0.0, 0.0, 0.0]
    DEFAULT_MAX = [100.0, 100.0, 100.0]

    def __init__(self, attr, nice_name, default_value, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        super(Long3Attribute, self).__init__(attr, nice_name, default_value, const.ATYPE_LONG3)

    def _create_widget(self):
        return Float3Widget(self.data_type, self.name, self.default_value, self._min, self._max, self.nice_name)


class ByteAttribute(BaseAttribute):
    """
    ByteAttribute, inherits from BaseAttribute, for maya byte attributes
    """
    DEFAULT_MIN = 0.0
    DEFAULT_MAX = 100.0

    def __init__(self, attr, nice_name, default_value, min_=None, max_=None):
        if not min_:
            self._min = self.DEFAULT_MIN
        else:
            self._min = min_
        if not max_:
            self._max = self.DEFAULT_MAX
        else:
            self._max = max_

        super(ByteAttribute, self).__init__(attr, nice_name, default_value)

    def _create_widget(self):
        return FloatWidget(self.data_type, self.name, self.default_value, self._min, self._max,
                           slider=True, nice_name=self.nice_name)
