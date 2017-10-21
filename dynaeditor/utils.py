import os
import sys
from dynaeditor import const


def attr_mapping_to_dict(mapping):
    args = zip(const.ARG_KEYS, mapping)
    args = {key:value for key, value in args if value}
    return args


def in_maya_standalone():
    """
    check if the current python interpreter is maya standalone or not
    :return:
    """
    executable = os.path.split(sys.executable)[1]
    if executable == "mayapy.exe":
        return True
    return False
