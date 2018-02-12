## Main script to connect to website and post the temperature

from machine import ADC
import math
import urequests as requests
import json
import micropython
from machine import Timer

micropython.alloc_emergency_exception_buf(100)

adc = ADC(0)
adc_lst = {}
adc_avg = 0 

user = 'esp03'
password = 'DICKballs12'
headers = {'Content-Type': 'application/json'}
login_url = 'http://'+'192.168.2.50'+'/auth/login'
module_url = 'http://'+'192.168.2.50'+'/module'

boot_send_count = 0

def get_temperature():
	for i in range(0,10):
		adc_lst[i] = adc.read()
		global adc_avg
		adc_avg += (adc_lst[i]/10)
	voltage = (adc_avg/1024)
	temp = math.floor((voltage - .5)/(.9/90))
	adc_avg = 0
	return temp

class Requestor:
	'''Request Class for HTTP requests from the ESP8266'''
	def __init__(self, url, json=None, headers={}):
		self.url = url
		self.json = json
		self.headers = headers

	def poster(self):
		try:
			r = requests.post(self.url, json=self.json, headers=self.headers)
		except Exception:
			print('Could not send post request')
			return
		try:
			r.json()
		except ValueError:
			print('No JSON could be decoded')
			return
		return r.json()

def get_token():
	token_request = Requestor(login_url, json={'name':user, 'password':password}, headers=headers)
	token_json = token_request.poster()

	if not token_json:
		return
	elif (422 in token_json.values() or 500 in token_json.values()):
		print(token_json['response'])
		return
	else:
		token = token_json['token']
		return token

def send_temperature():
	token = get_token()
	if not token:
		return
	temperature = get_temperature()
	temperature_request = Requestor(module_url, json={'token':token, 'name':user, 'temperature':temperature}, headers=headers)
	temperature_json = temperature_request.poster()

	if not temperature_json:
		return
	elif(400 in temperature_json.values() or 404 in temperature_json.values()):
		print(temperature_json['response'])
		return
	else:
		print('Temperature %d Sent' % temperature)

print('Sending Temperature')
while (boot_send_count < 1):
	send_temperature()
	boot_send_count = boot_send_count + 1

Timer(-1).init(period=3600000, mode=Timer.PERIODIC, callback=lambda t:send_temperature())

