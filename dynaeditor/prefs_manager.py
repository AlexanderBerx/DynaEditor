import json
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

    @property
    def item_visibility_prefs(self):
        settings = QtCore.QSettings()
        size = settings.beginReadArray("visibility")
        visibility_prefs = []
        for index in range(size):
            settings.setArrayIndex(index)
            index_key = settings.childKeys()[0]
            value = settings.value(index_key)
            value = json.loads(value)
            visibility_prefs.append((index_key, value))
        settings.endArray()
        return visibility_prefs

    @item_visibility_prefs.setter
    def item_visibility_prefs(self, value):
        """
        :param list value:
        :return:
        """
        settings = QtCore.QSettings()
        settings.beginWriteArray("visibility")
        for index, value in enumerate(value):
            name, visibility = value
            settings.setArrayIndex(index)
            settings.setValue(name, visibility)

        settings.endArray()



def main():
    manager = PrefsManager()
    return manager

if __name__ == '__main__':
    main()
