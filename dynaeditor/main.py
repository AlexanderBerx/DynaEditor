import sys
import logging
from PySide2 import QtWidgets
from dynaeditor.controller import Editor
from dynaeditor.utils import general_utils


def init_logging():
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)


def main():
    init_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting up Dynamic Attribute Editor")
    app = None
    if general_utils.in_maya_standalone():
        app = QtWidgets.QApplication([])
        logger.debug("created QApplication")

    editor = Editor()
    editor.view.show()

    if general_utils.in_maya_standalone():
        logger.info("Executing QApplication")
        sys.exit(app.exec_())

    return editor

if __name__ == '__main__':
    editor = main()
