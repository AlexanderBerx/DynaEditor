import pytest
from dynaeditor.widgets.base_widget import BaseWidget


def test_base_widget():
    # check that base widget always expect arguments
    with pytest.raises(TypeError):
        BaseWidget()

    # base widget is an abstract class an will raise type errors when
    # being instanced directly
    with pytest.raises(NotImplementedError):
        BaseWidget('test_name', 'test_value')
