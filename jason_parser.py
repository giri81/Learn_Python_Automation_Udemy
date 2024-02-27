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


# Print the price of a title ie one among the many element in the json file
# Given the key as input
def fetch_price(json_file, title):
    with open(json_file, 'r') as f:
        data = json.load(f)
    courses = data.get('course_data', [])
    """"The get() method retrieves the value for the specified key ('course_data' 
    in this case) from the dictionary (data), and if the key is not found, it returns 
    the default value provided as the second argument, which in this case is an empty
     list ([]). 
    """

    for course in courses:
        if course['title'] == title:
            return course['price']
    return None


json_file = 'static_file_2.json'
title = input("Enter the title of the course: ")
price = fetch_price(json_file, title)
if price is not None:
    print(f"The price of '{title}' is: {price}")
else:
    print(f"Course '{title}' not found.")
