import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class BoolWidget(BaseWidget):
    def __init__(self, attribute_name, default_value):
        self._chb_bool = None
        super(BoolWidget, self).__init__(attribute_name, default_value)

    def create_type_widget(self):
        self._chb_bool = QtWidgets.QCheckBox()
        return self._chb_bool

    def set_default_value(self, default_value):
        self._chb_bool.setChecked(bool(default_value))


def main():
    app = QtWidgets.QApplication([])
    widget = BoolWidget("test", 1)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
