import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class EnumWidget(BaseWidget):
    def __init__(self, nice_name, default_value, options):
        self._cbo_enum = None # type: QtWidgets.QComboBox
        super(EnumWidget, self).__init__(nice_name, default_value)
        self.set_options(options)

    def create_type_widget(self):
        self._cbo_enum = QtWidgets.QComboBox()
        return self._cbo_enum

    def set_default_value(self, default_value):
        pass

    def get_value(self):
        return self._cbo_enum.currentIndex()

    def set_options(self, options):
        self._cbo_enum.clear()
        self._cbo_enum.addItems(options)


def main():
    app = QtWidgets.QApplication([])
    widget = EnumWidget("test", "")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
