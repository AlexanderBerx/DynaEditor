from dynaeditor import const


def attr_mapping_to_dict(mapping):
    args = zip(const.ARG_KEYS, mapping)
    args = {key:value for key, value in args if value}
    return args
