from PySide2 import QtWidgets


class BaseWidget(QtWidgets.QWidget):
    def __init__(self, attribute_name):
        super(BaseWidget, self).__init__()
        self._create_ui(attribute_name)

    def _create_ui(self, attribute_name):
        main_layout = QtWidgets.QGridLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(QtWidgets.QLabel(attribute_name))
        main_layout.addWidget(self._create_type_widget(), 0, 1)

        set_btn = QtWidgets.QPushButton("Set")
        main_layout.addWidget(set_btn, 0, 2)

    def _create_type_widget(self):
        """
        creates & returns the widget specific to the type of the widget,
        must be overwritten by child classes
        :return: QtWidgets.QWidget
        """
        raise NotImplementedError("Method must be overwritten in child Classes")
