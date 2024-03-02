'''
Created by Narendra for COMP216 October 2020
wk05_a8_read_session.py

Sessions are used to perserve data across request. Critical
to simulate state in http interaction.

'''

from flask.globals import request
import requests

URL = 'http://127.0.0.1:5000/read_session' 

s = requests.Session()

for _ in range(5):
    r = s.get(URL)
    print(r.text)
