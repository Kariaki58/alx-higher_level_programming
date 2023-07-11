#!/usr/bin/python3
"""script that adds all arguments to a python list"""


import sys
Python_list_data = __import__('5-save_to_json_file').save_to_json_file
json_list = __import__('6-load_from_json_file').load_from_json_file
if __name__ == "__main__":
    try:
        Python_list = json_list("add_item.json")
    except FileNotFoundError:
        Python_list = []
    Python_list.extend(sys.argv[1:])
    Python_list_data(Python_list, "add_item.json")
