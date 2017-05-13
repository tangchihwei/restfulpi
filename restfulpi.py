import requests
import json

backend = 'http://localhost:5000/'
headers = {'Content-type': 'application/json'}
cardid = {"id":"CLIPPER_CARD_001"} 

# resp = requests.post(backend+"scan", json.dumps(cardid), headers = headers)
resp = requests.get(backend+"user/"+str(cardid['id']))

# parse into json object
respJson = json.loads(resp.text)
print "User Name: "+respJson['who']
print "Account Balance: $"+str(respJson['balance'])
print "Last Trip: $"+str(respJson['lastTrip'])

data={ "id":"CLIPPERCARD_001", "agency":"BART",	"origin":"MONTGOMERY","destination":"MILLBRAE", "referral":"GOOGLE"}

resp = requests.post(backend+"ticket", json.dumps(data), headers = headers)
respJson = json.loads(resp.text)
print(str(respJson))