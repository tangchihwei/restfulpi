import requests
import json

backend = 'http://0.0.0.0:5000/scan'
headers = {'Content-type': 'application/json'}
data = {"id":"12667"} 


resp = requests.post(backend, json.dumps(data), headers = headers)
resp.json