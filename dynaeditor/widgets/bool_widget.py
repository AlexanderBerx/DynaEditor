import sys
try:
    from PySide2 import QtWidgets
except ImportError:
    from Qt import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class BoolWidget(BaseWidget):
    """
    BoolWidget class, inherits from BaseWidget, widget for displaying bool attributes
    """
    def __init__(self, type_, attr, default_value, nice_name=None):
        """
        initialise the widget
        :param str nice_name: nice name of the widget to be displayed
        :param bool default_value: default value of the widget
        """
        self._chb_bool = None
        super(BoolWidget, self).__init__(type_, attr, default_value, nice_name)

    def create_type_widget(self):
        """
        creates the type widget
        :return: QtWidgets.QCheckBox
        """
        self._chb_bool = QtWidgets.QCheckBox()
        return self._chb_bool

    def set_default_value(self, default_value):
        """
        sets the current value of the widget
        :param bool default_value: current value of the widget
        :return: None
        """
        self._chb_bool.setChecked(bool(default_value))

    def get_value(self):
        """
        returns the current value of the widget
        :return: Bool
        """
        return bool(self._chb_bool.isChecked())


def main():
    app = QtWidgets.QApplication([])
    widget = BoolWidget("tests", True)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
