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


