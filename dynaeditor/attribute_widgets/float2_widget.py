import sys
from PySide2 import QtWidgets
from dynaeditor.attribute_widgets.base_widget import BaseWidget
from dynaeditor.widgets.float_slider_widget import FloatSliderWidget


class Float2Widget(BaseWidget):
    """
    Float3Widget for displaying float3 attributes, inherits from BaseWidget
    """
    def __init__(self, data_type, attr, default_value, min_=None, max_=None, nice_name=None):
        """
        initialises the widget
        :param str nice_name: name of the widget to be displayed
        :param list default_value: default value of the widget, float list of length 3
        :param list min_: min value of the widget, float list of length 3
        :param list max_: max value of the widget, float list of length 3
        """
        super(Float2Widget, self).__init__(data_type, attr, default_value, nice_name)
        if min_:
            self.set_min(min_)
        if max_:
            self.set_max(max_)

    def create_type_widget(self):
        """
        creates & returns the type widget
        :return: QtWidgets.QWidget
        """
        widget_vector = QtWidgets.QWidget()
        layout_vector = QtWidgets.QHBoxLayout()
        layout_vector.setMargin(0)
        widget_vector.setLayout(layout_vector)

        self._ff_x = FloatSliderWidget(slider=False)
        layout_vector.addWidget(self._ff_x)

        self._ff_y = FloatSliderWidget(slider=False)
        layout_vector.addWidget(self._ff_y)

        return widget_vector

    def set_default_value(self, default_value):
        """
        sets the default value of the widget
        :param list default_value: default value of the widget, float list of length 2
        :return: None
        """
        self._ff_x.text = default_value[0]
        self._ff_y.text = default_value[1]

    def get_value(self):
        """
        returns the current value of the widget
        :return: list
        """
        return float(self._ff_x.text), float(self._ff_y.text)

    def set_min(self, _min):
        """
        set the minimum value of th widget
        :param list _min: min value of the widget, float list of length 2
        :return: list
        """
        self._ff_x.set_min(_min[0])
        self._ff_y.set_min(_min[1])

    def set_max(self, _max):
        """
        set the maximum value of th widget
        :param list _max: min value of the widget, float list of length 2
        :return: list
        """
        self._ff_x.set_max(_max[0])
        self._ff_y.set_max(_max[1])


def main():
    app = QtWidgets.QApplication([])
    widget = Float2Widget("", "tests", [1, 1, 1], [0, 0, 0])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()