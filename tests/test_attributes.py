import json
import pytest
from PySide2 import QtCore
from dynaeditor import widgets
from dynaeditor import attributes


def test_base_attribute():
    """
    test the BaseAttribute class
    :return: None
    """
    # test if abstraction is being enforced
    with pytest.raises(NotImplementedError):
        attributes.BaseAttribute("test", None, "some_attr")


def test_bool_attribute():
    """
    tests the BoolAttribute class
    :return: None
    """
    attr = "test_bool"
    nice_name = "test bool"
    bool_type = "bool"
    default_value = False
    bool_attr = attributes.BoolAttribute(attr, nice_name, default_value)

    # connect to the attr slot for signal testing
    @QtCore.Slot(str, str, str)
    def attr_slot(name, type_, value):
        assert name == attr
        assert type_ == bool_type
        # since the value isn't being changed in the test the emited
        # value needs to still match the default value
        assert json.loads(value) == default_value

    bool_attr.signal_apply_attr[str, str, str].connect(attr_slot)

    # check if the widget type is correct
    assert type(bool_attr.widget) == widgets.BoolWidget
    # check the type
    assert bool_attr.type_ == bool_type
    # check if the name was set correctly
    assert bool_attr.name == attr
    # test signals
    bool_attr.widget._emit_attr()
    # test arg validation
    assert attributes.BoolAttribute.validate_args(attr=attr, nice_name=nice_name) is True
    assert attributes.BoolAttribute.validate_args(attr=attr) is False
    assert attributes.BoolAttribute.validate_args(nice_name=nice_name) is False


def test_enum_attribute():
    """
    tests the EnumAttribute class
    :return: None
    """
    attr = "test_enum"
    nice_name = "test enum"
    enum_type = "enum"
    default_value = 2
    test_options = ["1", "2", "3", "4"]
    enum_attr = attributes.EnumAttribute(attr, nice_name, default_value, test_options)

    # connect to the attr slot for signal testing
    @QtCore.Slot(str, str, str)
    def attr_slot(name, type_, value):
        assert name == attr
        assert type_ == enum_type
        # since the value isn't being changed in the test the emited
        # value needs to still match the default value
        assert json.loads(value) == default_value

    enum_attr.signal_apply_attr[str, str, str].connect(attr_slot)

    # check if the widget type is correct
    assert type(enum_attr.widget) == widgets.EnumWidget
    # check the type
    assert enum_attr.type_ == enum_type
    # check if the name was set correctly
    assert enum_attr.name == attr
    # test signals
    enum_attr.widget._emit_attr()
    # test arg validation
    assert attributes.EnumAttribute.validate_args(attr=attr,
                                                  nice_name=nice_name,
                                                  default_value=default_value,
                                                  options=test_options) is True
    assert attributes.EnumAttribute.validate_args(attr=attr) is False


def test_float3_attribute():
    """
    tests the Float3Attribute class
    :return: None
    """
    attr = "test_float3"
    nice_name = "test float3"
    float3_type = "float3"
    default_value = [0.0, 0.0, 1.0]
    enum_attr = attributes.Float3Attribute(attr, nice_name, default_value)

    # connect to the attr slot for signal testing
    @QtCore.Slot(str, str, str)
    def attr_slot(name, type_, value):
        assert name == attr
        assert type_ == float3_type
        # since the value isn't being changed in the test the emited
        # value needs to still match the default value
        assert json.loads(value) == default_value

    enum_attr.signal_apply_attr[str, str, str].connect(attr_slot)

    # check if the widget type is correct
    assert type(enum_attr.widget) == widgets.Float3Widget
    # check the type
    assert enum_attr.type_ == float3_type
    # check if the name was set correctly
    assert enum_attr.name == attr
    # test signals
    enum_attr.widget._emit_attr()


def test_attribute():
    """
    tests the Attribute class
    :return: None
    """
    # attribute class needs to raise an type error if an type is not known to it
    with pytest.raises(TypeError):
        attributes.Attribute(_type="unknown")
