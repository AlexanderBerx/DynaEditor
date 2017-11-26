from PySide2 import QtCore
from dynaeditor.utils import general
from dynaeditor.model import EditorModel, EditorProxyModel
from dynaeditor.attributewidgets.base import BaseWidget


def get_model():
    """
    creates and returns an instance of the EditorModel with test data loaded
    :return: EditorModel, dict
    """
    test_data = [("double3", "testAttr", "Test Attr", None, None, [0, 0, 0], None, False, False),
                 ("bool", "testAttr2", "Test Attr2", 0, 1, 0, None, False, False)]

    mapped_test_data = []
    for item in test_data:
        mapped_test_data.append(general.key_map_config(item))

    model = EditorModel()
    model._add_from_mappings(mapped_test_data)
    return model, mapped_test_data


def test_model():
    """
    tests if items are being registered within the model, and if the model is properly cleared
    :return: None
    """
    model, test_data = get_model()
    assert model.rowCount() == len(test_data)
    model.clear()
    assert model.rowCount() == 0


def test_model_data():
    """
    tests if the model returns the correct data for the corresponding roles
    :return: None
    """
    model = get_model()[0]
    for index in range(model.rowCount()):
        index = model.index(index)
        item_widget = model.data(index, EditorModel.WIDGET_ROLE)
        assert isinstance(item_widget, BaseWidget)


def test_model_proxy():
    """
    tests if the proxy model correctly filters out the 'invisible' items
    :return: None
    """
    model, test_data = get_model()
    proxy = EditorProxyModel()
    proxy.setSourceModel(model)

    assert proxy.rowCount() == len(test_data)

    # make all items 'invisible'
    for index in range(model.rowCount()):
        index = model.index(index)
        model.setData(index, False, QtCore.Qt.CheckStateRole)

    # when all items are made 'invisible' the proxy model shouldn't return any data
    assert proxy.rowCount() == 0


def test_model_proxy_data():
    """
    tests if the model proxy returns the expected data for the desired roles
    :return: None
    """
    model, test_data = get_model()
    proxy = EditorProxyModel()
    proxy.setSourceModel(model)
    # Note: it's intended behaviour for the proxy model to not return data for
    # the checkstaterole and the display role, since the data will be shown
    # through the widget
    for index in range(proxy.rowCount()):
        index = proxy.index(index, 1)
        assert proxy.data(index, QtCore.Qt.CheckStateRole) is None
        assert proxy.data(index, QtCore.Qt.DisplayRole) is None
