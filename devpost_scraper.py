import requests
from bs4 import BeautifulSoup

page_num = 2
hackathons_url = f'https://devpost.com/hackathons?page={page_num}'
r = requests.get(hackathons_url)
soup = BeautifulSoup(r.content, features='lxml')

# print(soup.prettify())
hackathons = soup.find_all('h2')
for hackathon in hackathons:
    print(hackathon.text.strip())
