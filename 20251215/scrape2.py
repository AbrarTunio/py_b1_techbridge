import requests
from bs4 import BeautifulSoup

url = "https://codepro.com.pk"
response = requests.get( url )

allcodehtml =  response.text

parsedData = BeautifulSoup(  allcodehtml   ,   'html.parser'  ) 

listItems = parsedData.find_all('li' , class_='nav-item')
hash = parsedData.find_all('h1' )
anchors = parsedData.find_all('a')
# print(listItems)

# for l , h in zip( hash, listItems ):
#     l = l.text.strip()
#     h = h.text.strip()
#     print(l , "---" , h  )

for x in listItems:
    print(x.text)

for a in anchors:
    print( a['href'] )