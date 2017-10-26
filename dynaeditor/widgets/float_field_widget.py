from PySide2 import QtWidgets, QtGui


class FloatField(QtWidgets.QLineEdit):
    WIDTH = 75
    def __init__(self, _min=0.0, _max=10000000.0, decimals=5):
        super(FloatField, self).__init__()
        self._validator = QtGui.QDoubleValidator(_min, _max, decimals)
        self.setValidator(self._validator)

        self.set_min(_min)
        self.set_max(_max)

        self.setMinimumWidth(self.WIDTH)
        self.setMaximumWidth(self.WIDTH)

    def set_min(self, _min):
        self._validator.setBottom(_min)

    def set_max(self, _max):
        self._validator.setTop(_max)
