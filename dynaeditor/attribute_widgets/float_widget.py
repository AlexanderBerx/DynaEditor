import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.float_field_widget import FloatField
from dynaeditor.attribute_widgets.base_widget import BaseWidget

class FloatWidget(BaseWidget):
    def __init__(self, data_type, attr, default_value, nice_name=None):
        super(FloatWidget, self).__init__(data_type, attr, default_value, nice_name)

    def create_type_widget(self):
        """
        creates & returns the type widget of the EnumWidget
        :return: QtWidgets.QComboBox
        """
        self._float_field = FloatField()
        return self._float_field

    def set_default_value(self, default_value):
        """
        set the default value of the combobox by index, if the given value
        is higher then the item count nothing the index of the combobox won't
        be change
        :param int default_value: index of the default value
        :return: None
        """
        self._float_field.setText(str(default_value))

    def get_value(self):
        return float(self._float_field.text())


def main():
    app = QtWidgets.QApplication([])
    widget = FloatWidget("", "test", 0.1)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
