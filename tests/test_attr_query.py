from dynaeditor import attrquery
from dynaeditor.utils import general
from maya import cmds

TEST_ATTRS = [('bool', 'test_bool', 'tests bool', 0.0, 1.0, 0.0, None, False, False),
              ('enum', 'test_enum', 'tests enum', 0.0, 3.0, 0.0,
               ['test1', 'test2', 'test3', 'test4'], False, False)]


def _add_test_attrs_to_node(node):
    cmds.select(node)
    for attr_setup in TEST_ATTRS:
        # unpack setup values
        creation_args = general.key_map_config_maya(attr_setup)
        cmds.addAttr(**creation_args)


def create_test_node():
    """
    creates an node of 'unknown' type and ads custom attributes to it for testing
    :return: str
    """
    node = cmds.createNode("unknown")
    _add_test_attrs_to_node(node)
    return node


def test_query():
    test_node = create_test_node()
    # collect all the obj attrs
    obj_attrs = list(attrquery.iter_obj_attrs(test_node))
    # check if each tests attr occurs in the object attr's & matches
    for attr in TEST_ATTRS:
        if attr not in obj_attrs:
            raise ValueError("attr not returned from query")
