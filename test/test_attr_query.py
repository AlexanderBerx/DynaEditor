import pytest
from dynaeditor import utils

try:
    from maya import cmds
    if utils.in_maya_standalone():
        from maya import standalone
except ImportError:
    print("Can't run tests due to no maya modules present in current environment")
    raise


class TestAttrQuery(object):
    @classmethod
    def setup_class(cls):
        """
        sets up a maya test env to test the attr query module
        :return: None
        """
        if utils.in_maya_standalone():
            standalone.initialize()

    @classmethod
    def teardown_class(cls):
        if utils.in_maya_standalone():
            standalone.uninitialize()

    def _add_test_attrs_to_node(node):
        pass

    def create_test_node(self):
        """
        creates an node of 'unknown' type and ads custom attributes to it for testing
        :return: str
        """
        node = cmds.createNode("unknown")
        self._add_test_attrs_to_node(node)
        return node

    def test_something(self):
        test_node = self.create_test_node()
        print(test_node)
        print("testing something")
