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
    name = hackathon.find('h2').text.strip()
    if len(name) <= 1:
        name = '<No Name>'
    print(name)
    url = hackathon.a.get('href')
    soup = get_page(url)
    eligibility = soup.find(id='challenge-eligibility')
    if eligibility is None:
        continue
    eligibility_text = eligibility.get_text().strip()
    print(eligibility_text.lstrip('Eligibility').strip())
    print('-' * 80)
