# Script for creating a room called Webhooks on WebEx
import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = getpass('Paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {
	'title': 'Webhooks'
}

bodyJSON = json.dumps(body)

headers = {
	'Authorization': 'Bearer ' + TOKEN,
	'Content-Type': 'application/json'
}

createRoom = BASEURL + room

response = requests.post(createRoom, headers=headers, data=bodyJSON)

responseJSON = response.json()

pprint(responseJSON)

