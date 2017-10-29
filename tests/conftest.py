from PySide2 import QtWidgets
try:
    from maya import standalone
except ImportError:
    raise EnvironmentError("Can't run tests due to no maya modules present in current environment")


def pytest_sessionstart(session):
    """ before session.main() is called. """
    # NOTE: the QApplication has to be created before maya is initialized
    QtWidgets.QApplication([])
    standalone.initialize()


def pytest_sessionfinish(session, exitstatus):
    """ whole tests run finishes. """
    standalone.uninitialize()
