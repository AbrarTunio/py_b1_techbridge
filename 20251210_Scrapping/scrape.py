# pip install requests
import requests

url = "https://codepro.com.pk"
response = requests.get(url)

print( response.status_code )
print( response.text )

