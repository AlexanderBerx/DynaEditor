import os
import json
from dynaeditor.utils import general_utils
from dynaeditor.controller import Editor


def test_app():
    """
    tests if the whole app runs
    :return:
    """
    editor = Editor()
    test_data = os.path.split(__file__)[0]
    test_data = os.path.join(test_data, "../rsc/test_data.json")
    test_data = os.path.abspath(test_data)
    with open(test_data, 'r') as file_in:
        data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(item) for item in data]
    editor.set_editor_options(mapped_data)
