"""API automation . Source of API end points and related documentation is available at
   https://rahulshettyacademy.com/practice-project
   Base url is http://216.10.245.166

    Credits:
    - Original author: Rahul Shetty , udemy.com
    - Contributor: Girish Devappa
    - Date: Feb 28th 2024
"""
import requests
import json

# HTTP method to test GET, use query parameter
# API endpoint http://216.10.245.166/Library/GetBook.php
response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty'}, )
# request.get method accepts query parameters as a dictionary
# headers are option here so 3rd arg is blank

#print(response.text)
#print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response[0]['isbn'])

# response.json method will return a json format response
json_response = response.json()

print(type(json_response))
print(json_response[0]['isbn'])

# Monitor response headers via assert
# Note: Headers are retunred as dictionary

# Validate if header 'Content-Type' is 'application/json;charset=UTF-8'
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Validate response status code using assert
#assert response.status_code == 200
print(response.status_code)

# Retrieve the book details with ISBN RGHCC
# Get all the books and iterate

flag = False # to know if found or not for print
for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        flag = True
        break

if not flag:
    print("RGHCC isbn book not present")

expectedBook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239"
}

assert actualBook == expectedBook
