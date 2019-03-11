import urllib.request
from bs4 import BeautifulSoup
import pprint


# http://tracker.flightview.com/customersetup/FlightViewWebFids/cachedFids/?vmode=departures&Apt=FRA&mainPage=tracker.flightview.com
link_all = "https://tracker.flightview.com/FVAccess2/tools/fids/fidsDefault.asp?accCustId=FVWebFids&fidsId=20001&fidsInit=departures&fidsApt=FRA&fidsFilterAl=&fidsFilterArrap="
# https://www.google.com/flights#flt=FRA.KTW.2019-03-24*KTW.FRA.2019-03-28;c:UAH;e:1;sd:1;t:f
# link = "https://www.flightview.com/airport/FRA/departures"

link_delay = "https://flightaware.com/live/cancelled/today/FRA"

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('div', style="float: left; display: inline-block; max-width: 74%")
    cont = table.find_all('h3')
    preres =  [str(i).replace("<h3>", "").replace("</h3>", "").replace("\xa0\xa0", "  ") for i in cont]
    return [int(i.split("  ")[1]) for i in preres]

def parse_a(html):
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find_all('td', id="ffAlLbl")
    # for i in table:

    return len(table)

res1 = parse_a(get_html(link_all))
res2 = parse(get_html(link_delay))
pprint.pprint(res1)
pprint.pprint(res2)
print((res2[0] + res2[2])/res1)