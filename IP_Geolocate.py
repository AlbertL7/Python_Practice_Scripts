import requests
import json

key = 'API_KEY'

ip_address = input("IPv4/IPv6 ")

request = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={ip_address}")

print(request)

response = json.loads(request.content)

print(json.dumps(response, indent=4))
