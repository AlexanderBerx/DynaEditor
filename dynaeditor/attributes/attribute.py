from dynaeditor import const
from dynaeditor.attributes.attribute_types import BoolAttribute
from dynaeditor.attributes.attribute_types import EnumAttribute
from dynaeditor.attributes.attribute_types import FloatAttribute
from dynaeditor.attributes.attribute_types import Float2Attribute
from dynaeditor.attributes.attribute_types import Float3Attribute


class Attribute(object):
    """
    Factory class for creating attribute attributes
    """
    TYPE_MAPPING = {const.ATYPE_ENUM: EnumAttribute,
                    const.ATYPE_BOOL: BoolAttribute,
                    const.ATYPE_FLOAT3: Float3Attribute,
                    const.ATYPE_FLOAT2: Float2Attribute,
                    const.ATYPE_FLOAT: FloatAttribute}

    def __new__(cls, type_, *args, **kwargs):
        """
        creates and attribute of the given _type with the given options
        if the given type is not supported a TypeError will be raised
        :param str type_: name of the wanted type
        :return: Attribute
        """
        _class = Attribute.get_class_for_type(type_)
        return _class(*args, **kwargs)

    @staticmethod
    def get_class_for_type(type_):
        """
        staticmethod, returns the class of the given _type,
        if the given type can't be found an TypeError will be raised
        :param str type_: type name of the attribute
        :return: cls
        """
        for keys, _class in Attribute.TYPE_MAPPING.items():
            if type_ == keys:
                return _class
        raise TypeError("Not Implemented type: {}".format(type_))

    @staticmethod
    def is_type_supported(type_):
        """
        static method which checks if the given attribute type is supported or not
        :param type_: 
        :return: bool
        """
        if type_ in Attribute.TYPE_MAPPING.keys():
            return True
        return False
