from PySide2 import QtWidgets, QtGui, QtCore


class FloatSliderWidget(QtWidgets.QWidget):
    WIDTH = 50

    def __init__(self,  min_=0.0, max_=100.0, decimals=5, slider=True):
        super(FloatSliderWidget, self).__init__()
        self._create_ui(min_, max_, decimals, slider)
        self._connect_signals(slider)

        self.set_min(min_)
        self.set_max(max_)
        self.text = (max_ - min_)/2.0

    def _create_ui(self, min_, max_, decimals, slider):
        layout = QtWidgets.QHBoxLayout()
        layout.setMargin(0)
        self.setLayout(layout)

        if slider:
            self._slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            self._slider.setRange(min_, max_)
            layout.addWidget(self._slider)

        self._txt_field = QtWidgets.QLineEdit()
        self._txt_field.setMinimumWidth(self.WIDTH)
        self._txt_field.setMaximumWidth(self.WIDTH)
        layout.addWidget(self._txt_field)
        self._validator = QtGui.QDoubleValidator(min_, max_, decimals)
        self._txt_field.setValidator(self._validator)

    def set_min(self, min_):
        """
        sets the minimum value of the widget
        :param float min_: minimum value of the widget
        :return: None
        """
        self._validator.setBottom(float(min_))


    def set_max(self, max_):
        """
        sets the maximum value of the widget
        :param float max_: maximum value of the widget
        :return: None
        """
        self._validator.setTop(float(max_))

    @property
    def text(self):
        return self._txt_field.text()

    @text.setter
    def text(self, value):
        self._txt_field.setText(str(value))

    def _connect_signals(self, slider):
        if slider:
            self._txt_field.textChanged[str].connect(self._text_change)
            self._slider.valueChanged[int].connect(self._slider_change)

    @QtCore.Slot(int)
    def _slider_change(self, value):
        self.text = value

    @QtCore.Slot(str)
    def _text_change(self, value):
        self._slider.setValue(float(value))


def main():
    app = QtWidgets.QApplication([])
    widget = FloatSliderWidget(slider=False)
    widget.show()
    app.exec_()


if __name__ == '__main__':
    main()
