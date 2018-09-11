import machine
import urequests 
import json

adc = machine.ADC(0)
voltage = (((adc.read() *3.3)/1024)-0.5)*100

dat = {"device": "1","hashkey": "supersecret", "data": {"2": "1010"}}

url = 'http://192.168.0.129:5000/adddata'

headers = {'content-type': 'application/json'}

response = urequests.post(url, data=json.dumps(dat), headers=headers)


response = urequests.post(url, data = dat)
print(response)
data = dict(data='{"device": "1","hashkey": "supersecret", "data": {"2": "1010"}}')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = urequests.post(url, data=urlencode(data), headers=headers)
print(response.json())
