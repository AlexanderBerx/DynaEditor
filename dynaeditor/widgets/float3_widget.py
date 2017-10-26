import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget
from dynaeditor.widgets.float_field_widget import FloatField


class Float3Widget(BaseWidget):
    def __init__(self, nice_name, default_value):
        super(Float3Widget, self).__init__(nice_name, default_value)

    def create_type_widget(self):
        widget_vector = QtWidgets.QWidget()
        layout_vector = QtWidgets.QHBoxLayout()
        widget_vector.setLayout(layout_vector)

        self._ff_x = FloatField()
        layout_vector.addWidget(self._ff_x)

        self._ff_y = FloatField()
        layout_vector.addWidget(self._ff_y)

        self._ff_z = FloatField()
        layout_vector.addWidget(self._ff_z)

        return widget_vector

    def set_default_value(self, default_value):
        if not len(default_value) == 3:
            return

        self._ff_x.setText(default_value[0])
        self._ff_y.setText(default_value[1])
        self._ff_z.setText(default_value[2])

    def get_value(self):
        return self._ff_x.text(), self._ff_y.text(), self._ff_z.text()


def main():
    app = QtWidgets.QApplication([])
    widget = Float3Widget("test", [1, 1, 1])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
