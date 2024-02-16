'''
Created by Narendra for COMP216 October 2020
wk05_a6_get_cookie.py

Reads a cookie
'''

import requests

URL = 'https://google.com'                       #this site uses cookies           
# URL = 'https://centennialcollege.ca'             #this site uses cookies           
URL_SEND = 'http://127.0.0.1:5000/set_cookies'            #request all users 
URL_READ = 'http://127.0.0.1:5000/get_cookies'            #request all users 

s = requests.Session()
s.get(URL_SEND)
s.get(URL_READ)

# d = s.cookies.get_dict()                         #get the data as a dict
for k, v in s.cookies.get_dict().items():                         
    print(f'{k}: {v}')                           #print the key and the value