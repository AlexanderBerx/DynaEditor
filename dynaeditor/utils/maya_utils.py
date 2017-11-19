import logging
from maya import cmds


def get_first_selected_node():
    """
    returns the first selected shape node, if transform nodes are selected
    the children of the transform node will be checked first for shape nodes
    :return: str
    """
    logger = logging.getLogger(__name__)
    logger.debug("Getting first selected shape")
    for obj in cmds.ls(selection=True, long=True):
        if not cmds.objectType(obj) == "transform":
            return obj

        logger.debug("checking children of: {}".format(obj))
        child_shapes = cmds.listRelatives(obj, fullPath=True, ad=True) or []
        child_shapes = cmds.ls(child_shapes, long=True, shapes=True)
        if child_shapes:
            return child_shapes[0]
    logger.debug("No non transform nodes selected")


def _get_selection_shapes(node_type, get_children=True, same_type=False):
    """
    returns all the selected shape nodes according to the given parameters
    :param str node_type: type of the desired node
    :param bool get_children: get the children of the selection
    :param bool same_type: returns only shape nodes of the same type as the node_type
    :return: list
    """
    item_list = cmds.ls(selection=True, long=True)
    if get_children:
        item_list.extend((cmds.listRelatives(item_list, ad=True, f=True) or []))
    else:
        item_list.extend((cmds.listRelatives(item_list, c=True, f=True) or []))

    if same_type:
        item_list = cmds.ls(item_list, type=node_type, long=True)
    else:
        item_list = cmds.ls(item_list, shapes=True, long=True)

    return set(item_list)

def _apply_attr_to_node(node, attr_name, attr_value, attr_type=None):
    try:
        if attr_type:
            if isinstance(attr_value, list):
                cmds.setAttr("{0}.{1}".format(node, attr_name), *attr_value, type=attr_type)
                return True
            else:
                cmds.setAttr("{0}.{1}".format(node, attr_name), attr_value, type=attr_type)
                return True
        else:
            if isinstance(attr_value, list):
                cmds.setAttr("{0}.{1}".format(node, attr_name), *attr_value)
                return True
            else:
                cmds.setAttr("{0}.{1}".format(node, attr_name), attr_value)
                return True
    except (RuntimeError, ValueError) as e:
        logger = logging.getLogger(__name__)
        logger.warning("Failed to apply attribute to: {}".format(node))
        logger.warning("Error:".format(e))
        return False

def apply_attr(attr_name, attr_value, node_type, attr_type=None, affect_children=True, same_type=False):
    """
    applies the give attribute to all the selected nodes according to the parameters
    :param attr_name:
    :param attr_value:
    :param node_type:
    :param attr_type:
    :param affect_children:
    :param same_type:
    :return: int
    """
    logger = logging.getLogger(__name__)
    logger.info("Applying attr: {}".format(attr_name))
    logger.info("Attr type: {}".format(attr_type))
    logger.info("Attr value: {}".format(attr_value))
    applied_items = 0
    for node in _get_selection_shapes(node_type, affect_children, same_type):
        if _apply_attr_to_node(node, attr_name, attr_value, attr_type):
            logger.info("Applied attr to: {}".format(node))
            applied_items += 1

    logger.info("Applied attr to {} objects".format(applied_items))
    return applied_items
