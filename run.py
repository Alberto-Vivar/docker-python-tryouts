from bs4 import BeautifulSoup
import requests

r = requests.request('GET',
                     'https://www.ikea.com/es/es/p/billy-oxberg-libreria-modextensalt-puertpnl-vdr-blanco-vidrio-s49398857/')
soup = BeautifulSoup(r.text, features="html.parser")
text = soup.find(attrs={"class": "js-available-for-delivery"}).find(attrs={"class": "range-revamp-stockcheck__text"}).get_text()
print(text)
