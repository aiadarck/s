import requests
from bs4 import BeautifulSoup

url = "https://siatech.cloud/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

token = soup.find('input', {'name': '__RequestVerificationToken'})['value']
print( token)