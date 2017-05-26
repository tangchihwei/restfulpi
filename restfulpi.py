import requests
import json
import time
import Adafruit_BBIO.UART as UART
import serial
import sys
import binascii
import Adafruit_PN532 as PN532

_cmd_left_on = bytearray([0x7E, 0x80, 0x00, 0x01, 0x00, 0x00, 0x80, 0xAA, 0x00, 0x01, 0x01, 0x00, 0xDE, 0x62, 0x7E])
_cmd_right_on = bytearray([0x7E, 0x80, 0x00, 0x01, 0x00, 0x00, 0x80, 0xAA, 0x00, 0x01, 0x02, 0x00, 0x8B, 0x31, 0x7E])

class GflGate():
	def __init__(self, CS, MOSI, MISO, SCLK):
		#Backend
		self._backend = 'http://localhost:5000/'
		self._backend_heroku = 'https://gfl-turnstile.herokuapp.com/'
		self._backend = 'https://gfl-turnstile.herokuapp.com/'
		self._headers = {'Content-type': 'application/json'}
		self._pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

	def setup(self):
		# TODO: check BB-UAR1 HW config
		print "Initializing PN532 NFC Driver"
		self._pn532.begin()
		ic, ver, rev, support = self._pn532.get_firmware_version()
		print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
		self._pn532.SAM_configuration()
		# TODO:check if pn532 fail..?

		#Init UART1 bus on Beaglebone Black Wireless
		UART.setup("UART1")
		self.ser = serial.Serial(port = "/dev/ttyS1", baudrate = 19200)
		self.ser.close()
		self.ser.open()
		# TODO: return True/False for setup
	def reset_balance(self):
		resp = requests.get(self._backend + "startDemo")

	def hello(self):
		return "Hello GFL"

	def tap_request(self, card_id):
		HEADERS = {'Content-Type': "application/json"}
		BODY = { "cardId": str(card_id),
				"agency": "BART",
				"location": "MONTGOMERY",
				"machineId": "BART_M_0001"
				}
		tap_resp = requests.post(self._backend + "tap", headers=HEADERS, data=json.dumps(BODY))
		return json.loads(tap_resp.text) #return dictionary form

	def _turn_on_left_gate(self):
		print "turn on left gate"
		self.ser.write(_cmd_left_on)
		#TODO: wait and confirm return message

	def _turn_on_right_gate(self):
		print "turn on right gate"
		self.ser.write(_cmd_right_on)
		#TODO: wait and confirm return message

	def read_card(self):
		uid = self._pn532.read_passive_target()
		if uid is None:
			return None
		return_message = ('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
		print return_message
		return return_message

	def gate_control(self, direction):
		# TODO: call gate control 
		print "Opening Gate" + str(direction)

	def run(self):
		_card_present = False

		while True:
			card_id = self.read_card()
			if card_id is None:
				continue
                        else:
                            print("how do I open gate?")
			# print "Received here: " + str(card_id)
			resp = self.tap_request(card_id)
			print "User Name: "+ str(resp)
                        if resp["response"]["allowAccess"]:
                            self._turn_on_right_gate()

			time.sleep(2) #debounce time?

if __name__ == "__main__":
	gate = GflGate('P8_7', 'P8_8', 'P8_9','P8_10')
	gate.setup()
	print(gate.hello())
	#resp = gate.tap_request("CLIPPER_CARD_001")
	#print "User Name: "+str(resp)
	gate.run()
