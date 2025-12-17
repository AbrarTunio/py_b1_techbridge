import json
import requests

url = "https://abrartunio.github.io/myjsontest/product.json"

response = requests.get(url)

data = response.json()

title = data['title']
products = data['products']
services = data['services']


print(title)
for product in products:
    print(product)
for service in services:
    print(service)