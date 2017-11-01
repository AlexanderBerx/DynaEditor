import os
import sys
import json
import logging
from PySide2 import QtWidgets, QtCore
from dynaeditor.controller import Editor
from dynaeditor.utils import general_utils


def load_test_data(editor):
    logger = logging.getLogger(__name__)
    logger.debug("Loading Test data")
    with open(r"C:\Workspace\DynaEditor\rsc\test_data.json", "r") as file_in:
        test_data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(data) for data in test_data]

    editor.set_editor_options(mapped_data)


def load_resources():
    rsc_file = os.path.split(__file__)[0]
    rsc_file = os.path.join(rsc_file, "../bin/resources.rcc")
    rsc_file = os.path.abspath(rsc_file)
    if not os.path.isfile(rsc_file):
        return
    resources = QtCore.QResource()
    print resources.registerResource(rsc_file)
    print resources.children()
    print resources.data()


def init_logging():
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)


def main():
    load_resources()
    init_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting up Dynamic Attribute Editor")
    app = None
    if general_utils.in_maya_standalone():
        app = QtWidgets.QApplication([])
        logger.debug("created QApplication")

    editor = Editor()
    editor.view.show()

    #load_test_data(editor)

    if general_utils.in_maya_standalone():
        logger.info("Executing QApplication")
        sys.exit(app.exec_())

    return editor

if __name__ == '__main__':
    editor = main()
