import pytest
from dynaeditor import attributewidgets


def test_base_widget():
    """
    tests the BaseWidget class
    :return: None
    """
    # base widget is an abstract class an will raise type errors when
    # being instanced directly
    with pytest.raises(NotImplementedError):
        attributewidgets.BaseWidget(None, None, None)


def test_bool_widget():
    widget_bool = attributewidgets.BoolWidget('', 'test bool', True)
    assert isinstance(widget_bool.get_value(), bool)


def test_enum_widget():
    test_options = [1, 2, 3]
    test_value = 2
    widget_enum = attributewidgets.EnumWidget('', 'test_enum', test_value, test_options)

    assert widget_enum.get_value() == test_value
    assert widget_enum._cbo_enum.count() == len(test_options)


def test_float3_color_widget():
    test_value = [1, 0, 0]
    widget_float3_color = attributewidgets.Float3ColorWidget('', '', test_value)
    assert widget_float3_color.get_value() == test_value


def test_float3_widget():
    test_value = [1.0, 0.0, 0.0]
    test_min = [0.0, 0.0, 0.0]
    test_max = [1.0, 1.0, 1.0]
    widget_float3 = attributewidgets.Float3Widget('', '', test_value, test_min, test_max)

    # test the default value
    assert list(widget_float3.get_value()) == test_value
