import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class EnumWidget(BaseWidget):
    def __init__(self, nice_name, default_value):
        self._cbo_enum = None
        super(EnumWidget, self).__init__(nice_name, default_value)

    def create_type_widget(self):
        self._cbo_enum = QtWidgets.QComboBox()
        return self._cbo_enum

    def set_default_value(self, default_value):
        pass


def main():
    app = QtWidgets.QApplication([])
    widget = EnumWidget("test", "")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
