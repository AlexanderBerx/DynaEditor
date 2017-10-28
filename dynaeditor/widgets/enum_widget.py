import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class EnumWidget(BaseWidget):
    """
    EnumWidget class, inherits from BaseWidget for displaying enum attributes
    """
    def __init__(self, nice_name, default_value, options):
        """
        initialise the widget
        :param str nice_name: nice name of the widget to be displayed
        :param int default_value: index of the default value
        :param list options: str list of the options of the widget
        """
        self._cbo_enum = None  # type: QtWidgets.QComboBox
        super(EnumWidget, self).__init__(nice_name, default_value)
        self.set_options(options)
        self.set_default_value(default_value)

    def create_type_widget(self):
        """
        creates & returns the type widget of the EnumWidget
        :return: QtWidgets.QComboBox
        """
        self._cbo_enum = QtWidgets.QComboBox()
        return self._cbo_enum

    def set_default_value(self, default_value):
        """
        set the default value of the combobox by index, if the given value
        is higher then the item count nothing the index of the combobox won't
        be change
        :param int default_value: index of the default value
        :return: None
        """
        if default_value > self._cbo_enum.count():
            return
        self._cbo_enum.currentIndex(int(default_value))

    def get_value(self):
        """
        returns the index of the currently displayed item
        :return: int
        """
        return self._cbo_enum.currentIndex()

    def set_options(self, options):
        """
        set the options of widgets by list, clears the current options
        before setting them
        :param list options: list of strings containing the options
        :return: None
        """
        self._cbo_enum.clear()
        self._cbo_enum.addItems(options)


def main():
    app = QtWidgets.QApplication([])
    widget = EnumWidget("test", 1, [])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
