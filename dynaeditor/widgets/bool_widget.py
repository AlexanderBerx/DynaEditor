import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class BoolWidget(BaseWidget):
    def __init__(self, attribute_name):
        super(BoolWidget, self).__init__(attribute_name)

    def _create_type_widget(self):
        self._bool_chb = QtWidgets.QCheckBox()
        return self._bool_chb


def main():
    app = QtWidgets.QApplication([])
    widget = BoolWidget("test")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
