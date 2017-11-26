"""
note module is called float_ and not float due to that it would otherwise
overshadow python's float class
"""
import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.floatslider import FloatSliderWidget
from dynaeditor.attribute_widgets.base import BaseWidget


class FloatWidget(BaseWidget):
    def __init__(self, data_type, attr, default_value, min_=0.0, max_=10000.0, slider=False, nice_name=None):
        self._create_slider = slider
        super(FloatWidget, self).__init__(data_type, attr, default_value, nice_name)
        self.set_min(min_)
        self.set_max(max_)

    def create_type_widget(self):
        """
        creates & returns the type widget of the FloatWidget
        :return: FloatSliderWidget
        """
        self._float = FloatSliderWidget(slider=self._create_slider)
        return self._float

    def set_default_value(self, default_value):
        self._float.text = default_value

    def get_value(self):
        return float(self._float.text)

    def set_min(self, value):
        self._float.set_min(float(value))

    def set_max(self, value):
        self._float.set_max(float(value))


def main():
    app = QtWidgets.QApplication([])
    widget = FloatWidget("", "test", 0.1)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
