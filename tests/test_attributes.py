import pytest
try:
    from PySide2 import QtCore
except ImportError:
    from Qt import QtCore
from dynaeditor import attribute_widgets
from dynaeditor import attributes


def test_base_attribute():
    """
    test the BaseAttribute class
    :return: None
    """
    # test if abstraction is being enforced
    attribute = attributes.BaseAttribute("test", "some_attr")
    with pytest.raises(NotImplementedError):
        attribute._create_widget()

def test_attribute():
    # attribute class needs to raise an type error if an type is not known to it
    with pytest.raises(TypeError):
        attributes.Attribute(_type="unknown")


def test_bool_attribute():
    attr = "test_bool"
    nice_name = "test bool"
    default_value = False
    bool_attr = attributes.BoolAttribute(attr, nice_name, default_value)


    # check if the widget type is correct
    assert type(bool_attr.widget) == attribute_widgets.BoolWidget
    # check the type
    assert bool_attr.data_type == ""
    # check if the name was set correctly
    assert bool_attr.name == attr


def test_enum_attribute():
    attr = "test_enum"
    nice_name = "test enum"
    enum_type = ""
    default_value = 2
    test_options = ["1", "2", "3", "4"]
    enum_attr = attributes.EnumAttribute(attr, nice_name, default_value, test_options)

    # check if the widget type is correct
    assert type(enum_attr.widget) == attribute_widgets.EnumWidget
    # check the type
    assert enum_attr.data_type == enum_type
    # check if the name was set correctly
    assert enum_attr.name == attr


def test_float3_attribute():
    attr = "test_float3"
    nice_name = "test float3"
    float3_type = "float3"
    default_value = [0.0, 0.0, 1.0]
    enum_attr = attributes.Float3Attribute(attr, nice_name, default_value)

    # check if the widget type is correct
    assert type(enum_attr.widget) == attribute_widgets.Float3Widget
    # check the type
    assert enum_attr.data_type == float3_type
    # check if the name was set correctly
    assert enum_attr.name == attr
