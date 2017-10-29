import pytest
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
    pass
