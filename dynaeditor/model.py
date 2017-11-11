from PySide2 import QtCore
from dynaeditor.attributes.attribute import Attribute


class EditorModel(QtCore.QObject):
    def __init__(self):
        super(EditorModel, self).__init__()
        self.__attributes = []

    def set_attributes(self, attr_mappings):
        for mapping in attr_mappings:
            try:
                attribute = Attribute(**mapping)
            # skip not implemented types
            except TypeError as e:
                continue
            self.__attributes.append(attribute)
