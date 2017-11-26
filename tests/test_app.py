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
    test_data = os.path.join(test_data, "../resources/test_data.json")
    test_data = os.path.abspath(test_data)
    with open(test_data, 'r') as file_in:
        data = json.load(file_in)
    mapped_data = [general_utils.key_map_config(item) for item in data]
    editor.model._add_from_mappings(mapped_data)
