try:
    from PySide2 import QtCore, QtWidgets, QtGui
except ImportError:
    from Qt import QtCore, QtWidgets, QtGui

class ColorPickerWidget(QtWidgets.QWidget):
    def __init__(self):
        super(ColorPickerWidget, self).__init__()
        self._color = QtGui.QColor()
        self._create_ui()
        self._connect_signals()

    @property
    def color(self):
        """
        :return: QtGui.QColor
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self._update_to_color(value)

    def _create_ui(self):
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.setMargin(0)
        self.setLayout(main_layout)

        self._btn_pick = QtWidgets.QPushButton()
        self._btn_pick.setAutoFillBackground(True)
        main_layout.addWidget(self._btn_pick)

        self._slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self._slider.setRange(0, 255)
        main_layout.addWidget(self._slider)

    def _connect_signals(self):
        self._btn_pick.clicked.connect(self.pick_color)
        self._slider.valueChanged[int].connect(self._slider_change)

    def pick_color(self):
        color = QtWidgets.QColorDialog.getColor(parent=self)  # type: QtGui.QColor
        if not color:
            return
        self.color = color

    @QtCore.Slot(int)
    def _slider_change(self, value):
        color = self.color
        hue = color.hue()
        saturation = color.saturation()
        alpha = color.alpha()
        color.setHsv(hue, saturation, value, alpha)
        self.color = color

    def _update_to_color(self, color):
        """
        :param QtGui.QColor color:
        :return:
        """
        self._btn_pick.setStyleSheet("QPushButton {{ background-color: {} }}".format(color.name()))
        self._slider.setValue(color.value())
