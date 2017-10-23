import pytest
from dynaeditor import utils
from dynaeditor import attr_query

try:
    from maya import cmds
    if utils.in_maya_standalone():
        from maya import standalone
except ImportError:
    print("Can't run tests due to no maya modules present in current environment")
    raise


class TestAttrQuery(object):
    TEST_ATTRS = [('bool', 'test_bool', 'test bool', 0.0, 1.0, 0.0, None, False, False, ["tests"]),
                  ('enum', 'test_enum', 'test enum', 0.0, 3.0, 0.0,
                   ['test1', 'test2', 'test3', 'test4'], False, False, ["tests"])]

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

    def _add_test_attrs_to_node(self, node):
        cmds.select(node)
        for attr_setup in self.TEST_ATTRS:
            # unpack setup values
            creation_args = utils.key_map_config_maya(attr_setup)
            cmds.addAttr(**creation_args)

    def create_test_node(self):
        """
        creates an node of 'unknown' type and ads custom attributes to it for testing
        :return: str
        """
        node = cmds.createNode("unknown")
        self._add_test_attrs_to_node(node)
        return node

    def test_query(self):
        test_node = self.create_test_node()
        # collect all the obj attrs
        obj_attrs = list(attr_query.iter_obj_attrs(test_node))
        # check if each test attr occurs in the object attr's & matches
        for attr in self.TEST_ATTRS:
            assert attr in obj_attrs
