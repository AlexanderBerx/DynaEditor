import sys
from PySide2 import QtWidgets
from dynaeditor.widgets.base_widget import BaseWidget
from dynaeditor.widgets.float_field_widget import FloatField


class Float3Widget(BaseWidget):
    def __init__(self, nice_name, default_value, _min, _max):
        super(Float3Widget, self).__init__(nice_name, default_value)
        self.set_min(_min)
        self.set_max(_max)

    def create_type_widget(self):
        widget_vector = QtWidgets.QWidget()
        layout_vector = QtWidgets.QHBoxLayout()
        # layout_vector.setMargin(0)
        widget_vector.setContentsMargins(0)
        layout_vector.setMargin(0)
        layout_vector.setContentsMargins(0)
        widget_vector.setLayout(layout_vector)

        self._ff_x = FloatField()
        layout_vector.addWidget(self._ff_x)

        self._ff_y = FloatField()
        layout_vector.addWidget(self._ff_y)

        self._ff_z = FloatField()
        layout_vector.addWidget(self._ff_z)

        return widget_vector

    def set_default_value(self, default_value):
        self._ff_x.setText(str(default_value[0]))
        self._ff_y.setText(str(default_value[1]))
        self._ff_z.setText(str(default_value[2]))

    def get_value(self):
        return self._ff_x.text(), self._ff_y.text(), self._ff_z.text()

    def set_min(self, _min):
        self._ff_x.set_min(_min[0])
        self._ff_y.set_min(_min[1])
        self._ff_z.set_min(_min[2])

    def set_max(self, _max):
        self._ff_x.set_max(_max[0])
        self._ff_y.set_max(_max[1])
        self._ff_z.set_max(_max[2])


def main():
    app = QtWidgets.QApplication([])
    widget = Float3Widget("test", [1, 1, 1])
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
