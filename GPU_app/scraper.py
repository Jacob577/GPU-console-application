import requests
from bs4 import BeautifulSoup

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find(id='ResultsContainer')

# job_elems = results.find_all('section', class_='card-content')

# print(job_elems)

URL = 'https://www.amazon.de/-/en/ASUS-Strix-GeForce-Gaming-Graphics/dp/B086FRKXJX/ref=sr_1_1?dchild=1&keywords=2060&qid=1609713669&sr=8-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, features="lxml")

results = soup.find_all(page.content, features="lxml")
# job_elems = results.find_all('section', class_='card-content')

print(soup)