import os
import sys
import inspect
from dynaeditor import const


def key_map_config(config):
    args = zip(const.ARG_KEYS, config)
    args = {key:value for key, value in args if value}
    return args


def key_map_config_maya(config):
    args = zip(const.M_ARG_KEYS, config)
    args = {key:value for key, value in args if value}

    # note: maya expect enum options in a csv formatting
    if args.get(const.M_ATTR_ARG_OPTIONS):
        enum_options = ""
        for option in args[const.M_ATTR_ARG_OPTIONS]:
            enum_options += str(option) + ":"

        args[const.M_ATTR_ARG_OPTIONS] = enum_options

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


def reset_session(user_path=None):
    """
    reset the maya session by deleting all the loaded modules from the
    give user userPath if not path is provided the entire workspace is cleared
    will be reloaded
    Credits for this one go to: Nick Rodgers
    (https://medium.com/@nicholasRodgers/sidestepping-pythons-reload-function-without-restarting-maya-2448bab9476e)
    :param str user_path: all modules bellow this path will be reloaded
    :return: None
    """
    if not user_path:
        user_path = os.path.dirname(__file__)
        user_path = os.path.abspath(os.path.join(user_path, ("..")))

    user_path = user_path.lower()
    mod_to_delete = []

    for key, loaded_module in sys.modules.iteritems():
        try:
            mod_file_path = inspect.getfile(loaded_module).lower()
            if mod_file_path.startswith(user_path):
                mod_to_delete.append(key)
        except:
            pass

    for loaded_module in mod_to_delete:
        del (sys.modules[loaded_module])
