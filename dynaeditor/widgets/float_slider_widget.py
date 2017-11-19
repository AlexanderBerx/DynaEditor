from PySide2 import QtWidgets, QtGui, QtCore


class FloatSliderWidget(QtWidgets.QWidget):
    WIDTH = 50
    def __init__(self,  min_=0.0, max_=100.0, decimals=5):
        super(FloatSliderWidget, self).__init__()
        self._create_ui(min_, max_, decimals)
        self._connect_signals()
        self.text = (max_ - min_)/2

    def _create_ui(self, min_, max_, decimals):
        layout = QtWidgets.QHBoxLayout()
        layout.setMargin(0)
        self.setLayout(layout)

        self._slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self._slider.setRange(min_, max_)
        layout.addWidget(self._slider)

        self._txt_field = QtWidgets.QLineEdit()
        self._txt_field.setMinimumWidth(self.WIDTH)
        self._txt_field.setMaximumWidth(self.WIDTH)
        layout.addWidget(self._txt_field)
        validator = QtGui.QDoubleValidator(min_, max_, decimals)
        self._txt_field.setValidator(validator)

    @property
    def text(self):
        return self._txt_field.text()

    @text.setter
    def text(self, value):
        self._txt_field.setText(str(value))

    def _connect_signals(self):
        self._slider.valueChanged[int].connect(self._slider_change)
        self._txt_field.textChanged[str].connect(self._text_change)

    @QtCore.Slot(int)
    def _slider_change(self, value):
        self.text = value

    @QtCore.Slot(str)
    def _text_change(self, value):
        self._slider.setValue(float(value))


def main():
    app = QtWidgets.QApplication([])
    widget = FloatSliderWidget()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
