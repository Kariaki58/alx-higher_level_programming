#!/usr/bin/python3
"""script that adds all arguments to a python list"""
import sys



if __name__ == "__main__":
    Python_list_data = __import__('5-save_to_json_file').save_to_json_file
    json_list = __import__('6-load_from_json_file').load_from_json_file

    try:
        Python_list = json_list("add_item.json")
    except FileNotFoundError:
        Python_list = []
    for i in range(1, len(sys.argv)):
        Python_list.append(sys.argv[i])
    Python_list_data(Python_list, "add_item.json")
