import datetime
from fuzzywuzzy import fuzz
import urllib.request, ssl
from bs4 import BeautifulSoup
import json

class Aircraft:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return self.name + ' ' + self.year


class AircraftsNet:

    def __init__(self):
        self.craft_dat = []
        with open('aircrafts.csv', 'r') as (f):
            for i in f:
                line = i.strip().split(';')
                self.craft_dat.append(Aircraft(line[0], line[2]))

    def search_year(self, text):
        year = 0
        maxi = 0
        for i in self.craft_dat:
            text.lower()
            i.name.lower()
            Ratio = fuzz.ratio(text.lower(), i.name.lower())
            Partial_Ratio = fuzz.partial_ratio(text.lower(), i.name.lower())
            Token_Sort_Ratio = fuzz.token_sort_ratio(text.lower(), i.name.lower())
            Token_Set_Ratio = fuzz.token_set_ratio(text.lower(), i.name.lower())
            temp = (Ratio + Partial_Ratio + Token_Sort_Ratio + Token_Set_Ratio) / 4
            if temp > maxi:
                maxi = temp
                year = int(i.year)

        return year

    def delay_extender(self, delay, text):
        year = datetime.datetime.now().year
        return delay + (year - self.search_year(text)) / 1000


def format_flight(flight):
    try:
        let = flight[:2]
        num = int(flight[2:])
        with open('airlines_translator.csv', 'r') as (f):
            for i in f:
                line = i.strip().split(';')
                if line[0] == let:
                    let = line[1]

        return let + str(num)
    except Exception as a:
        print(a)
        return flight


def get_plane(flight):
    flight = format_flight(flight)
    url = ('https://flightaware.com/live/flight/{}').format(flight.upper().replace(' ', ''))
    print(url)
    gcontext = ssl.SSLContext()

    def get_html(url):
        response = urllib.request.urlopen(url, context=gcontext)
        return response.read()

    def parse(html):
        soup = BeautifulSoup(html, features='html.parser')
        table = soup.find_all('script')
        for i in table:
            if 'var trackpollBootstrap = ' in str(i):
                result = str(str(i.text).replace('var trackpollBootstrap = ', '').replace(';', ''))

        try:
            print("OK")
            diktik = json.loads(result)
            airline_logo = diktik['flights'][list(diktik['flights'].keys())[0]]['thumbnail']['imageUrl']
            airplane = diktik['flights'][list(diktik['flights'].keys())[0]]['aircraft']['friendlyType']
        except:
            airplane = "B737"
            airline_logo = "https://resource.alaskaair.net/-/media/Images/campaigns/2019-brand-campaign/AA_2019_New-Airplane-Icon_midB-01?v=1"

        print(airplane)
        return airplane, airline_logo

    return parse(get_html(url))