from PySide2 import QtWidgets
from dynaeditor import utils


def pytest_sessionstart(session):
    """ before session.main() is called. """
    try:
        from maya import cmds
        if utils.in_maya_standalone():
            from maya import standalone
    except ImportError:
        raise EnvironmentError("Can't run tests due to no maya modules present in current environment")

    if utils.in_maya_standalone():
        # NOTE: the QApplication has to be created before the maya is initialized
        QtWidgets.QApplication([])
        standalone.initialize()

def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    pass