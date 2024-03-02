'''
Created by Narendra for COMP216 October 2020 (modified June, 2021)
wk05_a6_spoof_user_agent.py

Send a request with spoofed header

Try changing the user agent from the following url:
https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/2
and then check the server console.

Some web-sites incorrectly uses user-agent to different 
content to client. A better way is to use feature detection.


'''

import requests

URL = 'http://127.0.0.1:5000/a5_user_agents'

# agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0'}
# agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

response = requests.get(URL, headers=None)
print(f'{response.text}')          #Check the server terminal for the headers
# print('The server sends back the user-agent (this is not normal)')
# print(response.text)