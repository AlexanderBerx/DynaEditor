import os
try:
    from maya import standalone
except ImportError:
    standalone = None
    raise ImportError("Can't run tests due to no maya modules present in current environment")
try:
    from PySide2 import QtWidgets
except ImportError:
    raise ImportError("Can't run tests due to no PySide2 present in current environment")


def pytest_sessionstart(session):
    """ before session.main() is called. """
    # skips all the usersetup.py modules
    os.environ['MAYA_SKIP_USERSETUP_PY'] = '1'
    # NOTE: the QApplication has to be created before maya is initialized
    QtWidgets.QApplication([])
    standalone.initialize()


def pytest_sessionfinish(session, exitstatus):
    """ whole tests run finishes. """
    standalone.uninitialize()
