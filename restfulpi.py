import requests
import json

backend = 'https://gfl-turnstile.herokuapp.com/scan'
headers = {'Content-type': 'application/json'}
data = {"id":"12667"} 

resp = requests.post(backend, json.dumps(data), headers = headers)

# parse into json object
respJson = json.loads(resp.text)
print respJson
