import requests
import json
import time

# cardid = {"id":"CLIPPER_CARD_001"} 

# resp = requests.post(backend+"scan", json.dumps(cardid), headers = headers)

data={ "id":"CLIPPERCARD_001", "agency":"BART",	"origin":"MONTGOMERY","destination":"MILLBRAE", "referral":"GOOGLE"}

# resp = requests.post(backend+"ticket", json.dumps(data), headers = headers)
# respJson = json.loads(resp.text)
# print(str(respJson))

class GflGate():
	def __init__(self):
		self._backend = 'http://localhost:5000/'
		self._headers = {'Content-type': 'application/json'}


	def hello(self):
		return "hello GFL"

	def tap_request(self, uid):
		tapResp = json.loads(requests.get(self._backend + "user/"+str(uid)).text)
		return tapResp #return dictionary form

	def run(self):
		_card_present = False

		while True:
			
			time.sleep(1)





if __name__ == "__main__":
	gate = GflGate()
	print(gate.hello())
	resp = gate.tap_request("CLIPPER_CARD_001")
	print "User Name: "+resp['who']
	gate.run()

