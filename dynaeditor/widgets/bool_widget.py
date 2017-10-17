import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget


class BoolWidget(BaseWidget):
    def __init__(self, attribute_name):
        super(BoolWidget, self).__init__(attribute_name)

    def create_type_widget(self):
        self._chb_bool = QtWidgets.QCheckBox()
        return self._chb_bool


def main():
    app = QtWidgets.QApplication([])
    widget = BoolWidget("test")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
