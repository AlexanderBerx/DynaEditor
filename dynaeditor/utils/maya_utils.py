from maya import cmds


def get_first_selected_node():
    """
    returns the first selected shape node, if transform nodes are selected
    the children of the transform node will be checked first for shape nodes
    :return: str
    """
    for obj in cmds.ls(selection=True, long=True):
        obj_type = cmds.objectType(obj)
        if not obj_type == "transform":
            return obj
        child_shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if child_shapes:
            return child_shapes[0]


def _get_selection_shapes(node_type, get_children=True, same_type=False):
    item_list = cmds.ls(selection=True, long=True)
    if get_children == True:
        item_list.extend((cmds.listRelatives(item_list, ad=True, f=True) or []))
    else:
        item_list.extend((cmds.listRelatives(item_list, c=True, f=True) or []))

    if same_type == True:
        item_list = cmds.ls(item_list, type=node_type, long=True)
    else:
        item_list = cmds.ls(item_list, shapes=True, long=True)

    return set(item_list)


def apply_attr(attr_name, attr_value, node_type, attr_type=None, affect_children=True, same_type=False):
    if attr_type:
        for shape in _get_selection_shapes(node_type, affect_children, same_type):
            if isinstance(attr_value, list):
                cmds.setAttr("{0}.{1}".format(shape, attr_name), *attr_value, type=attr_type)
    else:
        for shape in _get_selection_shapes(node_type, affect_children, same_type):
            cmds.setAttr("{0}.{1}".format(shape, attr_name), attr_value)

