import requests
from bs4 import BeautifulSoup


def get_page(url):
    """ Returns soup object for a provided url """
    r = requests.get(url)
    return BeautifulSoup(r.content, features='lxml')


page_num = 1
hackathons_url = f'https://devpost.com/hackathons?page={page_num}'
soup = get_page(hackathons_url)

# print(soup.prettify())
hackathons = soup.find_all('article', {'class': 'challenge-listing'})
for hackathon in hackathons:
    url = hackathon.a.get('href')
    print(url)
    soup = get_page(url)
    eligibility = soup.find(id='challenge-eligibility')
    print(eligibility.get_text().strip().replace('\n', '  '))
    break
