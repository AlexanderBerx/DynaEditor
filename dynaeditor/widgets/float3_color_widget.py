import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget
from dynaeditor.widgets.color_picker_widget import ColorPickerWidget

class Float3ColorWidget(BaseWidget):
    """
    Float3Widget for displaying float3 attributes, inherits from BaseWidget
    """
    def __init__(self, nice_name, default_value):
        """
        initialises the widget
        :param str nice_name: name of the widget to be displayed
        :param list default_value: default value of the widget, float list of length 3
        """
        super(Float3ColorWidget, self).__init__(nice_name, default_value)


    def create_type_widget(self):
        """
        creates & returns the type widget
        :return: ColorPickerWidget
        """
        self.color_picker = ColorPickerWidget()
        return self.color_picker

    def set_default_value(self, default_value):
        """
        sets the default value of the widget
        :param list default_value: default value of the widget, float list of length 3
        :return: None
        """
        pass

    def get_value(self):
        """
        returns the current value of the widget
        :return: list
        """
        return


def main():
    app = QtWidgets.QApplication([])
    widget = Float3ColorWidget("test", [1, 1, 1])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
