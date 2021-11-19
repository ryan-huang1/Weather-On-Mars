import requests
import json
import os

url = 'https://discord.com/api/v9/users/@me/settings'

data = {
    {'custom_status': {'text': 'coolbenio'}}
}

headers = {
    'authorization': os.getenv('authkey'),
    'content-type': 'application/json'
}

response = requests.patch(url, data=data, headers=headers)

response = json.loads(response.text)
print(response)
