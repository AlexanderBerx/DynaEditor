from dynaeditor import const
from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute


class Attribute(object):
    """
    Factory class for instancing attribute attributes
    """
    TYPE_MAPPING = {const.ATYPE_BOOL:BoolAttribute,
                    const.ATYPE_ENUM:EnumAttribute}

    def __new__(cls,_type, *args, **kwargs):
        for keys, _class in cls.TYPE_MAPPING.items():
            if _type == keys:
                break
        else:
            raise TypeError("Not Implemented type")

        return _class(*args, **kwargs)
