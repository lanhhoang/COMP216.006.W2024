'''
Created by Narendra for COMP216 June 2020 (modified June, 2021)
wk05_1d_client_headers.py

Send a request with  customized headers

Try changing the payload dictionary and check 
the server console to see the modified header.
'''

import requests

URL = 'http://127.0.0.1:5000/a4_headers'

payload = {'secret': 'h7#$@(&', 'name': 'narendra'}
r = requests.get(URL, headers=payload)
print(f'{r.text}')          #Check the server terminal for the headers
