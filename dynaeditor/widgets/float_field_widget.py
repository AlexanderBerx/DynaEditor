from PySide2 import QtWidgets, QtGui


class FloatField(QtWidgets.QLineEdit):
    """
    FloatField widget textfield for float values, inherits from QtWidgets.QLineEdit
    """
    WIDTH = 50
    def __init__(self, min_=0.0, max_=10000000.0, decimals=5):
        """
        initialises the widget
        :param float min_: minimum value of the widget
        :param float max_: maximum value of the widget
        :param int decimals: amount of decimals
        """
        super(FloatField, self).__init__()
        self._validator = QtGui.QDoubleValidator(min_, max_, decimals)
        self.setValidator(self._validator)

        self.set_min(min_)
        self.set_max(max_)

        self.setMinimumWidth(self.WIDTH)
        self.setMaximumWidth(self.WIDTH)

    def set_min(self, _min):
        """
        sets the minimum value of the widget
        :param float _min: minimum value of the widget
        :return: None
        """
        self._validator.setBottom(_min)

    def set_max(self, _max):
        """
        sets the maximum value of the widget
        :param float _max: maximum value of the widget
        :return: None
        """
        self._validator.setTop(_max)
