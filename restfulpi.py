import requests
import json
import time

class GflGate():
	def __init__(self):
		self._backend = 'http://localhost:5000/'
		self._headers = {'Content-type': 'application/json'}


	def hello(self):
		return "hello GFL"

	def tap_request(self, card_id):
		tapResp = json.loads(requests.get(self._backend + "user/"+str(card_id)).text)
		return tapResp #return dictionary form

	def read_card(self):
		return "CLIPPER_CARD_001"

	# def gate_control():

	def run(self):
		_card_present = False

		while True:
			card_id = self.read_card()
			if card_id is None:
				continue
			resp = self.tap_request(card_id)
			print "User Name: "+ resp['who']
			time.sleep(1)

if __name__ == "__main__":
	gate = GflGate()
	print(gate.hello())
	# resp = gate.tap_request("CLIPPER_CARD_001")
	# print "User Name: "+resp['who']
	gate.run()

