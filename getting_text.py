import requests
from bs4 import BeautifulSoup

URL = "https://quantamagazine.org"
page = requests.get(URL)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
