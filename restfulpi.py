import requests
import json

backend = 'localhost'
headers = {'Content-type': 'application/json'}
cardid = {"id":"CLIPPER_CARD_001"} 

# resp = requests.post(backend+"scan", json.dumps(cardid), headers = headers)
resp = requests.get(backend+"user/"+str(cardid['id']))

# parse into json object
respJson = json.loads(resp.text)
print "User Name: "+respJson['who']
print "Account Balance: $"+str(respJson['balance'])
print "Last Trip: $"+str(respJson['lastTrip'])
# print "Transit Agency: "+respJson['agency']
# print "Trip Origin: "+respJson['origin']
# print "Trip Destination: "+respJson['destination']
# print "Trip Referral: "+respJson['referral']

