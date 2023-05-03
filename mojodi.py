import requests
from bs4 import BeautifulSoup

payload = {
    'username': '0924407220',
    'password': '001112131415Mn'
}


with requests.Session() as session:

    response = session.get("https://siatech.cloud/")
    soup = BeautifulSoup(response.content, 'html.parser')
    token = soup.find('input', {'name': '__RequestVerificationToken'})['value']


    payload['__RequestVerificationToken'] = token


    response = session.post("https://siatech.cloud/account/login", data=payload)


    soup = BeautifulSoup(response.content, 'html.parser')
    balance = soup.find('div', {'class': 'wallet-balance'}).text.strip()
    print("s: ", balance)