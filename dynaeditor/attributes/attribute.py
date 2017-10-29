import logging
from dynaeditor import const
from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute
from dynaeditor.attributes.float3_attribute import Float3Attribute
from dynaeditor.attributes.attr_type_error import AttrTypeError


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
        logger = logging.getLogger(__name__)
        logger.debug("Creating attribute of type: {}".format(_type))
        logger.debug("args: {}".format(args))
        logger.debug("kwargs: {}".format(kwargs))
        _class = Attribute.get_class_for_type(_type)
        return _class(*args, **kwargs)

    @staticmethod
    def get_class_for_type(_type):
        for keys, _class in Attribute.TYPE_MAPPING.items():
            if _type == keys:
                return _class
        else:
            raise AttrTypeError("Not Implemented type: {}".format(_type))

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
        attr_class = Attribute.get_class_for_type(_type)
        return attr_class.validate_args(*args, **kwargs)
