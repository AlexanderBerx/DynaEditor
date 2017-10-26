from PySide2 import QtWidgets, QtGui


class FloatField(QtWidgets.QLineEdit):
    def __init__(self, _min=0.0, _max=10000000.0):
        super(FloatField, self).__init__()
        self._validator = QtGui.QDoubleValidator(_min, _max)
        self.setValidator(self._validator)

