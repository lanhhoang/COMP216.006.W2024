'''
Created by Narendra for COMP216 June 2021
wk05_a12_webservice_get.py

Send a GET request to a webservices
The server returns json document with entries like :
  "1": {
    "age": 24, 
    "domestic": true, 
    "fname": "Diego", 
    "gpa": 1.0, 
    "lname": "Roy", 
    "program": "3409", 
    "semester": 3
  }
'''

import requests
number_to_get = '5'
URL = f'http://127.0.0.1:5000/students/{number_to_get}'        #request all users

r = requests.get(URL, timeout=4)                 # make a HTTP GET request

if r.ok:                                         # check response status
    users = r.json()                             # get the json
    print(users)
else:                                                  
    print(r.status_code)                         # failure so display static code
