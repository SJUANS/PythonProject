"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""


def add_to_dict(dict_name,key="",value=""):
    is_in_dict = key in my_english_dict
    if type(dict_name) is not dict:
        type_of_1st_arg = type(dict_name)
        print(f'You need to send a dictionary. You sent: {type_of_1st_arg}')
    elif value=="":
        print('You need to send a word and a definition.')
    elif is_in_dict is True:
        print(f"{key} is already on the dictionary. Won't add.")
    else:
        my_english_dict[f"{key}"] = f"{value}"
        print(f"{key} has been added.")


def get_from_dict(dict_name,key=""):
    is_in_dict = key in my_english_dict
    if type(dict_name) is not dict:
        type_of_1st_arg = type(dict_name)
        print(f'You need to send a dictionary. You sent: {type_of_1st_arg}')
    elif key=="":
        print('You need to send a word to search for.')
    elif is_in_dict is False:
        print(f"{key} was not found in this dict.")
    else:
        print(f"{key}: {my_english_dict[key]}")


def update_word(dict_name,key="",value=""):
    is_in_dict = key in my_english_dict
    if type(dict_name) is not dict:
        type_of_1st_arg = type(dict_name)
        print(f'You need to send a dictionary. You sent: {type_of_1st_arg}')
    elif value=="":
        print('You need to send a word and a definition to update.')
    elif is_in_dict is False:
        print(f"{key} is not on the dict. Can't update non-existing word.")
    else:
        my_english_dict[key] = f"{value}"
        print(f"{key} has been updated to: {value}")


def delete_from_dict(dict_name,key=""):
    is_in_dict = key in my_english_dict
    if type(dict_name) is not dict:
        type_of_1st_arg = type(dict_name)
        print(f'You need to send a dictionary. You sent: {type_of_1st_arg}')
    elif key=="":
        print('You need to specify a word to delete.')
    elif is_in_dict is False:
        print(f"{key} is not in this dict. Won't delete.")
    else:
        del my_english_dict[key]
        print(f"{key} has been deleted.")


# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')

my_english_dict = {}

