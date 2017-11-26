"""
main app module, run the main module for starting up the app,
initializes logging and loads the necessary resources
"""
import os
import sys
import logging
from PySide2 import QtWidgets, QtCore
from dynaeditor.controller import Editor
from dynaeditor.utils import general


def load_resources():
    rsc_file = os.path.split(__file__)[0]
    rsc_file = os.path.join(rsc_file, "../bin/resources.rcc")
    rsc_file = os.path.abspath(rsc_file)
    if not os.path.isfile(rsc_file):
        return
    resources = QtCore.QResource()
    if resources.registerResource(rsc_file):
        raise RuntimeError("Failed to register resources")


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
    if general.in_maya_standalone():
        app = QtWidgets.QApplication([])
        logger.debug("created QApplication")

    dyna_editor = Editor()
    dyna_editor.view.show()

    if general.in_maya_standalone():
        logger.info("Executing QApplication")
        sys.exit(app.exec_())

    return dyna_editor


if __name__ == '__main__':
    editor = main()
