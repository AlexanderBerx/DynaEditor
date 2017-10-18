from dynaeditor.attributes.bool_attribute import BoolAttribute
from dynaeditor.attributes.enum_attribute import EnumAttribute


class AttrEditor(object):
    """
    Factory class for instancing attribute attributes
    """
    TYPE_MAPPING = {}
    def __new__(cls, *args, **kwargs):
        inst = cls()
        return inst()
