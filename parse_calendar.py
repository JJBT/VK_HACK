import requests
from bs4 import BeautifulSoup
import json


URL = "https://meloman.ru/calendar/"


def parse_calendar():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.find('div', id='isocontainer')

    events = []

    for elem in table.find_all('div', class_='calendar-day'):
        day_events = elem.find('ul')

        for ev in day_events.find_all('li'):

            data = ev.find('div', class_='hall-entry-body')\
                .find('div')

            link = None

            try:
                link = data.find('em').find('a').get('href')
            except:
                pass

            event = {'names': [names.text for names in data.find_all('strong')],
                     'link': link,
                     'day': int(elem.find('p', class_='day').text),
                     'month': elem.find('p', class_='month').text}
            print(event)

            events.append(event)

    json.dump(events, "calendar.json", indent=4, sort_keys=True)



