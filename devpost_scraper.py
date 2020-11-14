import requests
from bs4 import BeautifulSoup

r = requests.get('https://devpost.com/hackathons')
soup = BeautifulSoup(r.content, features='lxml')

# print(soup.prettify())
hackathons = soup.find_all('h2')
for hackathon in hackathons:
    print(hackathon.text.strip())
    break
