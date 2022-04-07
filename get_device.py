import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://netbox.wws.sony.com/api/dcim/devices/"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 9f4d87e7705ba5c62afdb29e37a40eb6017ccc5e'
}

response = requests.request("GET", url, verify=False, headers=headers, data=payload)
json_data = response.json()
# print(response.text)
pprint(json_data)
