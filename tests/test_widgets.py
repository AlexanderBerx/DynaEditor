import pytest
from PySide2 import QtGui
from dynaeditor import widgets

def test_base_widget():
    """
    tests the BaseWidget class
    :return: None
    """
    # check that base widget always expect arguments
    with pytest.raises(TypeError):
        widgets.BaseWidget()

    # base widget is an abstract class an will raise type errors when
    # being instanced directly
    with pytest.raises(NotImplementedError):
        widgets.BaseWidget('test_name', 'test_value')


def test_bool_widget():
    """
    tests the BoolWidget class
    :return: None
    """
    widget_bool = widgets.BoolWidget('test_bool', True)
    assert isinstance(widget_bool.get_value(), bool)


def test_color_picker_widget():
    """
    tests the ColorPickerWidget class
    :return: None
    """
    widget_picker = widgets.ColorPickerWidget()
    color = QtGui.QColor.fromRgb(255, 0, 0)
    widget_picker.color = color

    assert widget_picker.color == color
    assert widget_picker._slider.value() == color.value()


def test_enum_widget():
    """
    tests the EnumWidget class
    :return: None
    """
    test_options = [1, 2, 3]
    test_value = 2
    widget_enum = widgets.EnumWidget('test_enum', test_value, test_options)

    assert widget_enum.get_value() == test_value
    assert widget_enum._cbo_enum.count() == len(test_options)


def test_float3_color_widget():
    """
    tests the EnumWidget class
    :return: None
    """
    test_value = [1, 0, 0]
    widget_float3_color = widgets.Float3ColorWidget('test', test_value)
    assert widget_float3_color.get_value() == test_value


def test_float3_widget():
    """
    tests the Float3Widget class
    :return: None
    """
    test_value = [1.0, 0.0, 0.0]
    test_min = [0.0, 0.0, 0.0]
    test_max = [1.0, 1.0, 1.0]
    widget_float3 = widgets.Float3Widget('test', test_value, test_min, test_max)

    # test the default value
    assert list(widget_float3.get_value()) == test_value
