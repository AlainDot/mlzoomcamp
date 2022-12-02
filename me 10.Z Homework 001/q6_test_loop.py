import requests
import time

url = "http://localhost:9696/predict"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
idx = 0

while True:
    idx = idx + 1

    time.sleep(0.1)
    response = requests.post(url, json=client).json()
    print(idx , ' : ' ,  response)

    if idx > 10000:
        break

