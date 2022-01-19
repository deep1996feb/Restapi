import requests
import json

URL = "http://127.0.0.1:8000/empcreate/"

data = {
    'Name': 'Banmeet Singh',
    'Field': 'Army',
    'Employeeid': 101,
    'Address': 'Himachal'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
data = r.json()
print(data)