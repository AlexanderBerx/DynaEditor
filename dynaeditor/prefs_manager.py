from PySide2 import QtCore
from dynaeditor import const


class PrefsManager(object):
    """
    PrefsManager class, for managing app preferences,
    wraps around QtCore.QSettings
    """
    def __init__(self):
        self.set_settings()

    def set_settings(self):
        """
        sets the current settings QSettings to those of editor
        :return: None
        """
        QtCore.QSettings().setDefaultFormat(QtCore.QSettings.IniFormat)
        QtCore.QCoreApplication.setOrganizationName(const.ORGANISATION_NAME)
        QtCore.QCoreApplication.setApplicationName(const.APP_NAME)

    @property
    def window_pos(self):
        """
        reads and returns the main window pos from the preferences
        :return: QtCore.QPoint
        """
        settings = QtCore.QSettings()
        return settings.value(const.PREF_WINDOW_POS)

    @window_pos.setter
    def window_pos(self, value):
        """
        stores the main window pos to the preferences
        :return: None
        """
        settings = QtCore.QSettings()
        settings.setValue(const.PREF_WINDOW_POS, value)
        print settings.fileName()

    @property
    def window_size(self):
        """
        reads and returns the main window pos from the preferences
        :return: QtCore.QSize
        """
        settings = QtCore.QSettings()
        return settings.value(const.PREF_WINDOW_SIZE)

    @window_size.setter
    def window_size(self, value):
        """
        stores the main window size to the preferences
        :return: None
        """
        settings = QtCore.QSettings()
        settings.setValue(const.PREF_WINDOW_SIZE, value)

    @property
    def affect_children(self):
        settings = QtCore.QSettings()
        value = settings.value(const.PREF_AFFECT_CHILDREN, True)
        return bool(int(value))

    @affect_children.setter
    def affect_children(self, value):
        settings = QtCore.QSettings()
        settings.setValue(const.PREF_AFFECT_CHILDREN, int(value))

    @property
    def restrict_to_type(self):
        settings = QtCore.QSettings()
        value  = settings.value(const.PREF_RESTRICT_TO_TYPE, True)
        return bool(int(value))

    @restrict_to_type.setter
    def restrict_to_type(self, value):
        settings = QtCore.QSettings()
        settings.setValue(const.PREF_RESTRICT_TO_TYPE, int(value))

    @property
    def item_visibility_prefs(self):
        """
        reads and returns the item visibility preferences
        :return: dict
        """
        settings = QtCore.QSettings()
        if settings.value(const.PREF_VISIBILITY):
            return const.DEFAULT_HIDDEN_ITEMS

        size = settings.beginReadArray(const.PREF_VISIBILITY)
        visibility_prefs = {}
        for index in range(size):
            settings.setArrayIndex(index)
            index_key = settings.childKeys()[0]
            visibility_prefs.update({index_key: int(settings.value(index_key))})
        settings.endArray()
        return visibility_prefs

    @item_visibility_prefs.setter
    def item_visibility_prefs(self, value):
        """
        stores the given visibility preferences, before storing given preferences
        are merged with the old ones
        :param dict value:
        :return: None
        """
        prefs = self.item_visibility_prefs
        prefs.update(value)

        settings = QtCore.QSettings()
        settings.remove(const.PREF_VISIBILITY)
        settings.beginWriteArray(const.PREF_VISIBILITY, len(prefs.keys()))
        for index, item in enumerate(prefs.items()):
            name, visibility = item
            settings.setArrayIndex(index)
            settings.setValue(name, int(visibility))

        settings.endArray()


def main():
    manager = PrefsManager()
    return manager


if __name__ == '__main__':
    main()
