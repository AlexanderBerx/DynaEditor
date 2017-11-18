import sys
try:
    from PySide2 import QtWidgets
except ImportError:
    from Qt import QtWidgets
from dynaeditor.attribute_widgets.base_widget import BaseWidget
from dynaeditor.widgets.float_field_widget import FloatField


class Float3Widget(BaseWidget):
    """
    Float3Widget for displaying float3 attributes, inherits from BaseWidget
    """
    def __init__(self, data_type, attr, default_value, _min, _max, nice_name=None):
        """
        initialises the widget
        :param str nice_name: name of the widget to be displayed
        :param list default_value: default value of the widget, float list of length 3
        :param list _min: min value of the widget, float list of length 3
        :param list _max: max value of the widget, float list of length 3
        """
        super(Float3Widget, self).__init__(data_type, attr, default_value, nice_name)
        self.set_min(_min)
        self.set_max(_max)

    def create_type_widget(self):
        """
        creates & returns the type widget
        :return: QtWidgets.QWidget
        """
        widget_vector = QtWidgets.QWidget()
        layout_vector = QtWidgets.QHBoxLayout()
        layout_vector.setMargin(0)
        widget_vector.setLayout(layout_vector)

        self._ff_x = FloatField()
        layout_vector.addWidget(self._ff_x)

        self._ff_y = FloatField()
        layout_vector.addWidget(self._ff_y)

        self._ff_z = FloatField()
        layout_vector.addWidget(self._ff_z)

        return widget_vector

    def set_default_value(self, default_value):
        """
        sets the default value of the widget
        :param list default_value: default value of the widget, float list of length 3
        :return: None
        """
        self._ff_x.setText(str(default_value[0]))
        self._ff_y.setText(str(default_value[1]))
        self._ff_z.setText(str(default_value[2]))

    def get_value(self):
        """
        returns the current value of the widget
        :return: list
        """
        return float(self._ff_x.text()), float(self._ff_y.text()), float(self._ff_z.text())

    def set_min(self, _min):
        """
        set the minimum value of th widget
        :param list _min: min value of the widget, float list of length 3
        :return: list
        """
        self._ff_x.set_min(_min[0])
        self._ff_y.set_min(_min[1])
        self._ff_z.set_min(_min[2])

    def set_max(self, _max):
        """
        set the maximum value of th widget
        :param list _max: min value of the widget, float list of length 3
        :return: list
        """
        self._ff_x.set_max(_max[0])
        self._ff_y.set_max(_max[1])
        self._ff_z.set_max(_max[2])


def main():
    app = QtWidgets.QApplication([])
    widget = Float3Widget("tests", [1, 1, 1], [0, 0, 0], [1, 1, 1])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
