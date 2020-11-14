import requests
from bs4 import BeautifulSoup


def get_page(url):
    """ Returns soup object for a provided url """
    r = requests.get(hackathons_url)
    return BeautifulSoup(r.content, features='lxml')


page_num = 2
hackathons_url = f'https://devpost.com/hackathons?page={page_num}'
soup = get_page(hackathons_url)

# print(soup.prettify())
hackathons = soup.find_all('article', {'class': 'challenge-listing'})
for hackathon in hackathons:
    url = hackathon.a.get('href')
    soup = get_page(url)
    print(soup.find_all('article'))
    break
