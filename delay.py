import urllib.request
from bs4 import BeautifulSoup
import threading

# http://tracker.flightview.com/customersetup/FlightViewWebFids/cachedFids/?vmode=departures&Apt=FRA&mainPage=tracker.flightview.com
# link_all = "https://tracker.flightview.com/FVAccess2/tools/fids/fidsDefault.asp?accCustId=FVWebFids&fidsId=20001&fidsInit=departures&fidsApt=FRA&fidsFilterAl=&fidsFilterArrap="
# https://www.google.com/flights#flt=FRA.KTW.2019-03-24*KTW.FRA.2019-03-28;c:UAH;e:1;sd:1;t:f
# link = "https://www.flightview.com/airport/FRA/departures"

# link_delay = "https://flightaware.com/live/cancelled/yesterday/FRA"


class Delay:
    def __init__(self, code):
        self.code = code
        self.link_all = "https://tracker.flightview.com/FVAccess2/tools/fids/fidsDefault.asp?accCustId=FVWebFids&fidsId=20001&fidsInit=arrivals&fidsApt={}".format(
            code)
        self.link_delay = "https://flightaware.com/live/cancelled/yesterday/{}".format(code)
        print(self.link_all)

    @staticmethod
    def get_html(url):
        response = urllib.request.urlopen(url)
        return response.read()

    @staticmethod
    def parse(html):
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find('div', style="float: left; display: inline-block; max-width: 74%")
        cont = table.find_all('h3')
        preres = [str(i).replace("<h3>", "").replace("</h3>", "").replace("\xa0\xa0", "  ") for i in cont]
        return [int(i.split("  ")[1]) for i in preres]

    def alter_del(self):
        result = []
        html = self.get_html(self.link_all)
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find_all('form')
        length = len(table)
        for i in table:
            try:
                result.append(i.find_all('a')[0].text.strip())
            except:
                result.append("No Takeoff Info - Call Airline")
        # print(self.link_all)
        # print(length)
        # print(result)
        # print(result.count('No Recent Info - Call Airline'))
        # print(
        #     (result.count("Delayed") + result.count("Cancelled") + result.count("No Takeoff Info - Call Airline") - 2))
        # print((result.count("Delayed") + result.count("Cancelled") + result.count(
        #     "No Takeoff Info - Call Airline") - 2 + result.count('No Recent Info - Call Airline')) / length)
        return (result.count("Delayed") + result.count("Cancelled") + result.count(
            "No Takeoff Info - Call Airline") - 2 + result.count('No Recent Info - Call Airline') / 4) / length

    @staticmethod
    def parse_a(html):
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find_all('td', id="ffAlLbl")
        return len(table)

    def get_delay(self):
        res1 = self.parse_a(self.get_html(self.link_all))
        print("All:", res1)
        res2 = self.parse(self.get_html(self.link_delay))
        print("Delay:", res2)
        try:
            return (res2[0] + res2[2]) / res1
        except ZeroDivisionError:
            return 0

# res1 = parse_a(get_html(link_all))
# res2 = parse(get_html(link_delay))
# pprint.pprint(res1)
# pprint.pprint(res2)
# print((res2[0] + res2[2])/res1)


# a = Delay("IEV")
# b = Delay("FRA")
# print(b.alter_del())
# print(b.get_delay())
