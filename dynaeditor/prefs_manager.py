from PySide2 import QtCore
from dynaeditor import const


class PrefsManager(object):
    def __init__(self):
        self.set_settings()

    def set_settings(self):
        QtCore.QSettings().setDefaultFormat(QtCore.QSettings.IniFormat)
        QtCore.QCoreApplication.setOrganizationName(const.ORGANISATION_NAME)
        QtCore.QCoreApplication.setApplicationName(const.APP_NAME)

    @property
    def window_pos(self):
        settings = QtCore.QSettings()
        return settings.value("main_window/pos")

    @window_pos.setter
    def window_pos(self, value):
        settings = QtCore.QSettings()
        settings.setValue("main_window/pos", value)
        print settings.fileName()

    @property
    def window_size(self):
        settings = QtCore.QSettings()
        return settings.value("main_window/size")

    @window_size.setter
    def window_size(self, value):
        settings = QtCore.QSettings()
        settings.setValue("main_window/size", value)



def main():
    manager = PrefsManager()
    return manager

if __name__ == '__main__':
    main()
