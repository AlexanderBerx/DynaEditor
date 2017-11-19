import sys
try:
    from PySide2 import QtCore, QtWidgets, QtGui
except ImportError:
    from Qt import QtCore, QtWidgets, QtGui
from dynaeditor.attribute_widgets.base_widget import BaseWidget
from dynaeditor.widgets.color_picker_widget import ColorPickerWidget


class Float3ColorWidget(BaseWidget):
    """
    Float3Widget for displaying float3 attributes, inherits from BaseWidget
    """
    def __init__(self, data_type, attr, default_value, nice_name=None):
        """
        initialises the widget
        :param str nice_name: name of the widget to be displayed
        :param list default_value: default value of the widget, float list of length 3
        """
        self._color_picker = None
        super(Float3ColorWidget, self).__init__(data_type, attr, default_value, nice_name)

    def create_type_widget(self):
        """
        creates & returns the type widget
        :return: ColorPickerWidget
        """
        self._color_picker = ColorPickerWidget()
        return self._color_picker

    def set_default_value(self, default_value):
        """
        sets the default value of the widget
        :param list default_value: default value of the widget, float list of length 3
        :return: None
        """
        color = QtGui.QColor.fromRgbF(*default_value)
        self._color_picker.color = color

    def get_value(self):
        """
        returns the current value of the widget
        :return: list
        """
        color = self._color_picker.color
        value = list(color.getRgbF())
        value.pop(3)
        return value


def main():
    app = QtWidgets.QApplication([])
    widget = Float3ColorWidget("tests", [1, 1, 1])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
