from dynaeditor import const
from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute
from dynaeditor.attributes.float3_attribute import Float3Attribute


class Attribute(object):
    """
    Factory class for creating attribute attributes
    """
    TYPE_MAPPING = {const.ATYPE_ENUM: EnumAttribute,
                    const.ATYPE_BOOL: BoolAttribute,
                    const.ATYPE_FLOAT3: Float3Attribute}

    def __new__(cls, _type, *args, **kwargs):
        """
        creates and attribute of the given _type with the given options
        if the given type is not supported a TypeError will be raised
        :param str _type: name of the wanted type
        :return: Attribute
        """
        _class = Attribute.get_class_for_type(_type)
        return _class(*args, **kwargs)

    @staticmethod
    def get_class_for_type(_type):
        """
        staticmethod, returns the class of the given _type,
        if the given type can't be found an TypeError will be raised
        :param str _type: type name of the attribute
        :return: cls
        """
        for keys, _class in Attribute.TYPE_MAPPING.items():
            if _type == keys:
                return _class
        raise TypeError("Not Implemented type: {}".format(_type))

    @staticmethod
    def is_type_supported(_type):
        """
        static method which checks if the given attribute type is supported or not
        :param _type: 
        :return: bool
        """
        if _type in Attribute.TYPE_MAPPING.keys():
            return True
        return False

    @staticmethod
    def validate_attr_args(_type, *args, **kwargs):
        """
        validates the arguments for the class of the given type.
        If the given type can't be found an TypeError will be raised.
        :param str _type: name of the class type
        :param args:
        :param kwargs:
        :return: bool
        """
        attr_class = Attribute.get_class_for_type(_type)
        return attr_class.validate_args(*args, **kwargs)
