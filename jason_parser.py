"""Parse a json string to a dictionary using module method json.loads
   Parse a static json file using module method json.load
   Required to understand the json content structure using a json editor

    Credits:
    - Original author: Rahul Shetty , udemy.com
    - Contributor: Girish Devappa
    - Date: Feb 27th 2024
"""

import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

# Parse json string and return dictionary
dict_courses = json.loads(courses)
print(dict_courses)
print(dict_courses['name'])
# first language taught by trainer
print(dict_courses['languages'][0])


def print_json_keys(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        keys = data.keys()
        for key in keys:
            print(key)

# Specify the path to the complex JSON file
file_path = 'static_file.json'
print_json_keys(file_path)