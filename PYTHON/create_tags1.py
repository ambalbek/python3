import requests
import json
from pprint import pprint
r = requests.get('https://api.github.com/events')
# print(r.text())
json = r.json()
#data_list = json['payload']
for i in json:
    print(i)