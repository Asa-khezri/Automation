
from bs4 import BeautifulSoup as bs
import requests
from datetime import date, timedelta


    
def Extraction():
    all_names = []
    for i in range(4):
        week = date.today() + timedelta(days= - date.today().weekday() + 5)
        current_week = []
        billboard = requests.get('https://www.billboard.com/charts/artist-100/'+str(week + timedelta(days = -i*7)))
        soup = bs(billboard.content, 'html.parser')
        sections = soup.find_all('div', class_ = "o-chart-results-list-row-container")
        for section in sections:
            name = section.find('h3')
            current_week.append(name.text.strip())
        all_names.append(current_week)
    return all_names   