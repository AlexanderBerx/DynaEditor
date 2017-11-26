"""
attribute query module for querying the attributes from objects
and all of there settings
"""
import os
import json
from maya import cmds
from dynaeditor import const


def _unpack_result(result):
    """
    unpacks the given result if the result has
    an length of 1
    :param list result: result to unpack
    :return: int
    """
    if not result:
        return None
    elif len(result) == 1:
        return result[0]
    return result


def get_attr_type(node, attr):
    """
    returns the attribute type of the given attribute for the given object
    :param str node: maya object
    :param str attr: attribute of the given maya object
    :return: int
    """
    try:
        return cmds.attributeQuery(attr, node=node, attributeType=True)
    except RuntimeError:
        return None


def get_attr_min(node, attr):
    """
    returns the minimum value of the given attribute from the
    given object if applicable
    :param str node: maya object
    :param str attr: attribute of the given maya object
    :return: int
    """
    if cmds.attributeQuery(attr, node=node, minExists=True):
        _min = cmds.attributeQuery(attr, node=node, min=True)
        return _unpack_result(_min)


def get_attr_max(node, attr):
    """
    returns the maximum value of the given attribute from the
    given object if applicable
    :param str node: maya object
    :param str attr: attribute of the given maya object
    :return: int
    """
    if cmds.attributeQuery(attr, node=node, maxExists=True):
        _max = cmds.attributeQuery(attr, node=node, max=True)
        return _unpack_result(_max)


def get_attr_default_value(node, attr):
    """
    returns the default value of the given node if possible
    :param str node: maya object
    :param str attr: attribute of the given maya object
    :return: str
    """
    try:
        default_value = cmds.attributeQuery(attr, node=node, listDefault=True)
        return _unpack_result(default_value)
    except RuntimeError:
        return None


def get_attr_enum(node, attr):
    """
    if the given attribute of the given node is of type enum a list with
    all possible string options will be returned else None will be returned
    :param str node: maya object
    :param str attr: maya attribute
    :return: list
    """
    if not cmds.attributeQuery(attr, node=node, enum=True):
        return None
    # if the enum can't be displayed as a string no point to check it
    if not cmds.getAttr("{0}.{1}".format(node, attr), asString=True):
        return None

    attr_value = cmds.getAttr("{0}.{1}".format(node, attr))
    attr_range = cmds.attributeQuery(attr, node=node, range=True)
    attr_enum = []

    for i in range(int(attr_range[0]), int(attr_range[1]) + 1):
        cmds.setAttr("{0}.{1}".format(node, attr), i)
        value = cmds.getAttr("{0}.{1}".format(node, attr), asString=True)
        if not value:
            return attr_enum
        attr_enum.append(value)

    cmds.setAttr("{0}.{1}".format(node, attr), attr_value)
    return attr_enum


def iter_obj_attrs(obj):
    """
    iterates the given objects attributes and returns it in a tuple along with all it's settings
    the formatting is done in the following way:
    (_type, attr, nice_name, _min, _max, default_value, options, file_path, color, categories)
    :param str obj: maya object to fetch the attributes from
    :return: (str, str, str, int, int, int, list, bool, bool, list)
    """
    for attr in cmds.listAttr(obj, write=True):
        # if type fetching fails no point in checking further
        # same goes for child attrs
        _type = get_attr_type(obj, attr)
        if not _type or cmds.attributeQuery(attr, node=obj, listParent=True):
            continue

        nice_name = cmds.attributeQuery(attr, node=obj, niceName=True)
        _min = get_attr_min(obj, attr)
        _max = get_attr_max(obj, attr)
        default_value = get_attr_default_value(obj, attr)
        options = get_attr_enum(obj, attr)
        file_path = cmds.attributeQuery(attr, node=obj, usedAsFilename=True)
        color = cmds.attributeQuery(attr, node=obj, usedAsColor=True)

        yield _type, attr, nice_name, _min, _max, default_value, options, file_path, color


def iter_obj_attrs_mapped(obj):
    """
    iterates the given objects attributes and returns it in a tuple along with all it's settings
    the result will be packed in a dictionary, note not existing settings will be left out
    :param str obj: maya object
    :return: dict
    """
    for items in iter_obj_attrs(obj):
        attr = zip(const.ARG_KEYS, items)
        yield {key: value for key, value in attr if value}


def obj_attrs_to_file(obj, output):
    """
    write's out the attributes of the given object to the given
    .json file path
    :param str obj: obj to get the attributes from
    :param str output: output file path
    :return: None
    """
    output = os.path.normpath(output)
    with open(output, 'w') as file_out:
        json.dump(list(iter_obj_attrs(obj)), file_out, indent=4)
