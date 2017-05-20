import requests
import json
import time
import Adafruit_BBIO.UART as UART
import serial

_cmd_left_on = bytearray([0x7E, 0x80, 0x00, 0x01, 0x00, 0x00, 0x80, 0xAA, 0x00, 0x01, 0x01, 0x00, 0xDE, 0x62, 0x7E])
_cmd_right_on = bytearray([0x7E, 0x80, 0x00, 0x01, 0x00, 0x00, 0x80, 0xAA, 0x00, 0x01, 0x02, 0x00, 0x8B, 0x31, 0x7E])


class GflGate():
	def __init__(self):
		self._backend = 'http://localhost:5000/'
		self._headers = {'Content-type': 'application/json'}
		UART.setup("UART1")
		ser = serial.Serial(port = "/dev/ttyS1", baudrate = 19200)
		ser.close()
		ser.open()

	def hello(self):
		return "Hello GFL"

	def tap_request(self, card_id):
		tap_resp = json.loads(requests.get(self._backend + "user/"+str(card_id)).text)
		return tap_resp #return dictionary form

	def _turn_on_left_gate():
		print "turn on left gate"
		ser.write(_cmd_left_on)

	def _turn_on_right_gate():
		print "turn on right gate"
		ser.write(_cmd_right_on)

	def read_card(self):
		return "CLIPPER_CARD_001"
		#TODO: read card nfc interface

	def gate_control(self, direction):
		# TODO: call gate control 
		print "Opening Gate" + str(direction)

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

