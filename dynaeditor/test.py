import json

arg_keys = ["_type", "attr", "nice_name", "_min", "_max", "default_value", "options", "file_path", "color", "categories"]

def print_args(*args, **kwargs):
    print args
    print kwargs


mapping_file = r"C:\Workspace\DynaEditor\rsc\test_data.json"
with open(mapping_file, "r") as file_in:
    attr_mapping = json.load(file_in)

for attr in attr_mapping:
    args = zip(arg_keys, attr)
    mapping = {key:value for key, value in args if value}
    print_args(**mapping)
