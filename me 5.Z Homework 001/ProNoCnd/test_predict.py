# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:48:53 2022

"""

import requests
import json

"""customer =  {"reports": 0, 
             "share": 0.001694, 
             "expenditure": 0.12, 
             "owner": "yes"}
"""
customer =  {"reports": 0,
             "share": 0.245, 
             "expenditure": 3.438, 
             "owner": "yes"}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)
result = response.json()

print('result = \n', json.dumps(result, indent=2))