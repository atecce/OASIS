import json
import requests
from urllib2 import Request, urlopen
from math import sin, floor
import time

ACCESS_TOKEN = "91cde66f8744bddb93103e41e91e6016"
ACCOUNT_ID = "287788ab-c9d3-471a-b18f-8b35bb43d327"

COMMANDS_ENDPOINT = "http://api.autoponics.com/commands"
DATA_POINTS_ENDPOINT = "http://api.autoponics.com/data_points"
IMAGES_ENDPOINT = "http://api.autoponics.com/images.json"

CONTINUOUS_DATA_SOURCES = {"test_ph": 6,"test_ec": 4,"test_temp": 20}
BINARY_DATA_SOURCES = {"test_pump"}

i = 0
j = 0

headers = {
  'Content-Type': 'application/json',
  'Authorization': "Token token=\"%(token)s\"" % { 'token': ACCESS_TOKEN }
}

#def create_image():
 # headers = {
  #  'Authorization': "Token token=\"%(token)s\"" % { 'token': ACCESS_TOKEN }
  #}

  #files = {'image[file]': open('/home/anurag/xhab/lettuce.jpg', 'rb')}
  #data = {'image[account_id]': ACCOUNT_ID }

  #r = requests.post(IMAGES_ENDPOINT, data=data, files=files, headers=headers)
  

def create_image():
  headers = {
    'Authorization': "Token token=\"%(token)s\"" % { 'token': ACCESS_TOKEN }
  }

  files = {'image[file]': open('/home/anurag/xhab/lettuce.jpg', 'rb')}
  data = {'image[account_id]': ACCOUNT_ID, 'image[name]': 'camera1', 'image[timestamp]': int(time.time())  }

  r = requests.post(IMAGES_ENDPOINT, data=data, files=files, headers=headers)
  print r.text

def create_command():
  json = "{\"command\": { \"account_id\": \"7b089da0-561c-4d0c-8471-3551378bb247\", \"payload\": {\"pump1\": \"on\"}}}"
  request = Request(COMMANDS_ENDPOINT, data=json, headers=headers)
  response_body = urlopen(request).read()
  print response_body

def create_data_point(name, value):
  json = "{\"data_point\": {\"name\": \"%(name)s\", \"value\": %(value)f, \"timestamp\": %(time)s}}" % {'name': key, 'value': value, 'time': int(time.time())}
  request = Request(DATA_POINTS_ENDPOINT, data=json, headers=headers)
  response_body = urlopen(request).read()
  print response_body

while True:
  for key, scale in CONTINUOUS_DATA_SOURCES.iteritems():
    value = sin(i) + scale
    #create_data_point(key, value)
    i += 0.1

  for key in BINARY_DATA_SOURCES:
    value = floor(j % 2)
    #create_data_point(key, value)
    j += 1

  #create_command()
  create_image()

  time.sleep(2)
