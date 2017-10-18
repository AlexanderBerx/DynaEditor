from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute


class Attribute(object):
    """
    Factory class for instancing attribute attributes
    """
    TYPE_MAPPING = {["bool"]:BoolAttribute}
    def __new__(cls,_type, *args, **kwargs):
        for keys, _class in cls.TYPE_MAPPING.items():
            if _type in keys:
                break
        else:
            raise TypeError("Not Implemented type")

        instance = _class(*args, **kwargs)
        return instance
