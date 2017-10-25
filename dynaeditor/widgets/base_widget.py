import json
from PySide2 import QtWidgets, QtCore


class BaseWidget(QtWidgets.QWidget):
    signal_apply_attr = QtCore.Signal(str)

    def __init__(self, nice_name, default_value):
        super(BaseWidget, self).__init__()
        self._create_ui(nice_name)
        self.set_default_value(default_value)
        self.connect_signals()

    def _create_ui(self, nice_name):
        layout_main = QtWidgets.QGridLayout()
        self.setLayout(layout_main)

        layout_main.addWidget(QtWidgets.QLabel(nice_name))
        layout_main.addWidget(self.create_type_widget(), 0, 1)

        self._btn_set = QtWidgets.QPushButton("Set")
        layout_main.addWidget(self._btn_set, 0, 2)

    def create_type_widget(self):
        """
        creates & returns the widget specific to the type of the widget,
        must be overwritten by child classes
        :return: QtWidgets.QWidget
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
