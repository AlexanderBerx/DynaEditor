import abc
from PySide2 import QtWidgets


class BaseWidget(QtWidgets.QWidget):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        super(BaseWidget, self).__init__()
