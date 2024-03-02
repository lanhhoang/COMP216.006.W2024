'''
Created by Narendra for COMP216 October 2020
wk05_a6_download_file.py

Downloads a file from a 'real' web server
'''

import requests

pathname = 'client_download/text.txt'
requested_file = 'test.txt'
URL = f'http://127.0.0.1:5000/download/{requested_file}'           #request all users

r = requests.get(URL, stream=True)               # make a HTTP GET request

with open(pathname, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=50):  #ridiculously small size
        print('+', end='')                       #give ser feedback
        fd.write(chunk)                          #write the bit to file
    print('\n...download completed')             #complete