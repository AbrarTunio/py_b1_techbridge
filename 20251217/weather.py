import json
import requests


url = f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={apikey}"

response = requests.get(url)

data = response.json()

print(data[-1]['name'])
print(data[-1]['country'])