# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

url = "https://codepro.com.pk"
response = requests.get(url)

# print(response.status_code)
html = response.text

soup = BeautifulSoup(html, "html.parser")

title = soup.find("h1").text
print(title)