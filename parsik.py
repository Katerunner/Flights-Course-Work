import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find_all('span')
    table2 = soup.find_all('h2')
    result = {}
    counter = 0
    for i in table2[1:]:
        counter += 1
        if counter == 1:
            key = str(i.contents[0]) + " " + str(i.contents[-1])
            result[key] = {'depart': '', 'arriv': '', 'date': '', 'airline': ''}
        elif counter == 2:
            result[key]['depart'] += i.contents[0]
        else:
            result[key]['arriv'] += i.contents[0]
        if counter == 3:
            counter = 0
            key = ''
    # print("\n")
    counter = 0
    kluchi = list(result.keys())
    # print(kluchi)
    for i in table[4:-4]:
        if i.contents != []:
            result[kluchi[counter]]['airline'] = i.contents[0]
            result[kluchi[counter]]['date'] = table[0].contents[0]
            counter+=1
    return result

print(parse(get_html("https://www.flightstats.com/v2/flight-tracker/route/LWO/IEV/?year=2019&month=2&date=24&hour=12")))