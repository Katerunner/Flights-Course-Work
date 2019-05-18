import json
import urllib.request

api = "5bbba82fc9d0f4ff8427b5e8e90e2cde"
if api == "":
    api = input("Enter OpenWeather api key: ")


class Weather:
    """Represents weather object"""
    def __init__(self):
        """Initialization"""
        self.w_dat = None
        self.dat = {}
        self.description = 'light snow'

        with open("bin/weather.csv", 'r') as f:
            for i in f:
                temp = i.strip().split(";")
                self.dat[temp[1]] = [temp[2], temp[3]]


    @property
    def image(self):
        """Gets image from url"""
        if self.w_dat:
            return 'http://openweathermap.org/img/w/{}.png'.format(self.w_dat['weather'][0]['icon'])

    def danger(self):
        """Calculates and returns danger coef for the weather"""
        return float(self.dat[self.description.lower()][-1])/50

    def weather_coord(self, coord):
        """Returns weather by coordinates"""
        urll = "https://api.openweathermap.org/data/2.5/weather?lat="
        urll += str(coord['lat']) + "&lon=" + str(coord['lon']) + "&appid=" + api
        x = urllib.request.urlopen(urll)
        obj = json.loads(x.read())
        self.w_dat = obj
        # print(obj['weather'][0]['id'])
        self.description = obj['weather'][0]['description']
        return obj['weather'][0]['description']

    def weather_coord_forecast(self, coord, indate):
        """Returns weather forecast by coordinates"""
        urll = "https://api.openweathermap.org/data/2.5/forecast?lat="
        urll += str(coord['lat']) + "&lon=" + str(coord['lon']) + "&appid=" + api
        x = urllib.request.urlopen(urll)
        obj = json.loads(x.read())
        self.w_dat = obj
        weath_dikt = {}
        for i in obj['list']:
            date = i['dt_txt'].split()[0]
            weath = i['weather'][0]['description'].capitalize()
            if date not in weath_dikt:
                weath_dikt[date] = []
            weath_dikt[date].append(weath)
        try:
            self.description = weath_dikt[indate][len(weath_dikt[indate])//2]
            return weath_dikt[indate][len(weath_dikt[indate])//2].lower()
        except KeyError:
            self.description = self.weather_coord(coord)
            return self.weather_coord(coord).lower()


# a = Weather()
# a.weather_coord_forecast(Corray(50.40, 30.45), '2019-05-14')
# print(b)
# print(a.danger())
# print(weather_coord(50.40, 30.45))
