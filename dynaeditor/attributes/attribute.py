from dynaeditor import const
from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute
from dynaeditor.attributes.float3_attribute import Float3Attribute


class Attribute(object):
    """
    Factory class for instancing attribute attributes
    """
    # TYPE_MAPPING = {const.ATYPE_ENUM: EnumAttribute}
    # TYPE_MAPPING = {const.ATYPE_BOOL: BoolAttribute}
    TYPE_MAPPING = {const.ATYPE_FLOAT3: Float3Attribute}

    def __new__(cls, _type, *args, **kwargs):
        for keys, _class in cls.TYPE_MAPPING.items():
            if _type == keys:
                break
        else:
            raise TypeError("Not Implemented type")

        return _class(*args, **kwargs)

    @staticmethod
    def is_type_supported(_type):
        if _type in Attribute.TYPE_MAPPING.keys():
            return True
        return False
