from PySide2 import QtWidgets


class BaseWidget(QtWidgets.QWidget):
    def __init__(self, attribute_name, default_value):
        super(BaseWidget, self).__init__()
        self._create_ui(attribute_name)
        self.set_default_value(default_value)

    def _create_ui(self, attribute_name):
        layout_main = QtWidgets.QGridLayout()
        self.setLayout(layout_main)

        layout_main.addWidget(QtWidgets.QLabel(attribute_name))
        layout_main.addWidget(self.create_type_widget(), 0, 1)

        btn_set = QtWidgets.QPushButton("Set")
        layout_main.addWidget(btn_set, 0, 2)

    def create_type_widget(self):
        """
        creates & returns the widget specific to the type of the widget,
        must be overwritten by child classes
        :return: QtWidgets.QWidget
        """
        raise NotImplementedError("Method must be overwritten in child Classes")

    def set_default_value(self, default_value):
        raise NotImplementedError("Method must be overwritten in child Classes")