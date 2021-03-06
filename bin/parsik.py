import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    """Returns html for url"""
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    """Returns parsed data"""
    soup = BeautifulSoup(html, features='html.parser')
    table = soup.find_all('span')
    table2 = soup.find_all('h2')
    result = {}
    counter = 0
    for i in table2[1:]:
        counter += 1
        if counter == 1:
            key = str(i.contents[0]) + ' ' + str(i.contents[-1])
            result[key] = {'depart': '', 'arriv': '', 'date': '', 'airline': ''}
        else:
            if counter == 2:
                result[key]['depart'] += i.contents[0]
            else:
                result[key]['arriv'] += i.contents[0]
        if counter == 3:
            counter = 0
            key = ''

    counter = 0
    kluchi = list(result.keys())
    for i in table[4:-4]:
        if i.contents != []:
            result[kluchi[counter]]['airline'] = i.contents[0]
            result[kluchi[counter]]['date'] = table[0].contents[0]
            counter += 1

    return result


def flight(from_v, to_v, date):
    """Returns data for certain route"""
    date = date.split('.')
    url = 'https://www.flightstats.com/v2/flight-tracker/route/' + str(from_v) + '/' + str(to_v) + '/?year=' + date[
        2] + '&month=' + date[1] + '&date=' + date[0] + '&hour=12'
    print(url)
    result = []
    main_d = parse(get_html(url))
    if main_d == {}:
        return ['Nothing found']
    else:
        for i in main_d:
            result.append((str(i), str(main_d[i]['airline']), str(main_d[i]['depart']), str(main_d[i]['arriv'])))
        print(result)
        return result
