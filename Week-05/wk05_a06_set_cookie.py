'''
Created by Narendra for COMP216 October 2020
wk05_a7_set_cookie.py

Sends a cookie to a server
'''

import requests

URL = 'http://127.0.0.1:5000/set_cookies'            #request all users
# cookies = {'professor': 'Narendra Pershad', 'course': 'Networking for Software Developers'}
 
r = requests.get(URL)
if r.ok:
    print('Cookies successfuly written to client computer')
else:
    print('Could not write cookies to client machine')
