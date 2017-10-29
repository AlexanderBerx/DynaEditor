import json
from PySide2 import QtWidgets, QtCore


class BaseWidget(QtWidgets.QWidget):
    """
    Abstract widget class, serves as a base for all attribute widget classes
    child classes need to overwrite all abstract methods
    """
    signal_apply_attr = QtCore.Signal(str)
    SET_BTN_WIDTH = 50
    SPACER_WIDTH = 30

    def __init__(self, nice_name, default_value):
        super(BaseWidget, self).__init__()
        self._create_ui(nice_name)
        self.set_default_value(default_value)
        self.connect_signals()

    def _create_ui(self, nice_name):
        """
        creates the ui of the widget
        :param str nice_name: nice name of the attribute to be displayed
        :return: None
        """
        layout_main = QtWidgets.QGridLayout()
        layout_main.setMargin(1)
        self.setLayout(layout_main)

        layout_main.addWidget(QtWidgets.QLabel(nice_name))
        layout_main.addWidget(self.create_type_widget(), 0, 1, QtCore.Qt.AlignRight)

        spacer = QtWidgets.QSpacerItem(self.SPACER_WIDTH, 10)
        layout_main.addItem(spacer, 0, 2)

        self._btn_set = QtWidgets.QPushButton("Set")
        self._btn_set.setMaximumWidth(self.SET_BTN_WIDTH)
        self._btn_set.setMinimumWidth(self.SET_BTN_WIDTH)
        layout_main.addWidget(self._btn_set, 0, 3)

    def create_type_widget(self):
        """
        creates & returns the widget specific to the type of the widget,
        must be overwritten by child classes
        :return: QtWidgets.QLayout
        """
        raise NotImplementedError("Method must be overwritten in child Classes")

    def set_default_value(self, default_value):
        """
        set the default value of the widget must be overwritten by child classes
        :param default_value:
        :return:
        """
        raise NotImplementedError("Method must be overwritten in child Classes")

    def get_value(self):
        """
        returns the current value of the widget
        :return: object
        """
        raise NotImplementedError("no get value method implemented")

    def _emit_attr(self):
        """
        emits the current value of the widget as a string
        :return: None
        """
        value = self.get_value()
        value = json.dumps(value)
        self.signal_apply_attr.emit(value)

    def connect_signals(self):
        """
        connect the signals of the widget
        :return: None
        """
        self._btn_set.clicked.connect(self._emit_attr)
