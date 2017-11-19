import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.float_slider_widget import FloatSliderWidget
from dynaeditor.attribute_widgets.base_widget import BaseWidget


class FloatWidget(BaseWidget):
    def __init__(self, data_type, attr, default_value, nice_name=None):
        super(FloatWidget, self).__init__(data_type, attr, default_value, nice_name)

    def create_type_widget(self):
        """
        creates & returns the type widget of the FloatWidget
        :return: FloatSliderWidget
        """
        self._float = FloatSliderWidget(slider=False)
        return self._float

    def set_default_value(self, default_value):
        self._float.text = default_value

    def get_value(self):
        return float(self._float.text)


def main():
    app = QtWidgets.QApplication([])
    widget = FloatWidget("", "test", 0.1)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
