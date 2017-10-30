from maya import cmds


def get_first_selected_shape():
    """
    returns the first selected shape node, if transform nodes are selected
    the children of the transform node will be checked first for shape nodes
    :return: str
    """
    selection = cmds.ls(selection=True, long=True)
    for obj in selection:
        obj_type = cmds.objectType(obj)
        if not obj_type == "transform":
            return obj
        child_shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if child_shapes:
            return child_shapes[0]

