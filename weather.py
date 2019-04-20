import json
import urllib.request

api = "5bbba82fc9d0f4ff8427b5e8e90e2cde"
if api == "":
    api = input("Enter OpenWeather api key: ")


class Weather:
    def __init__(self):
        self.w_dat = None
        self.dat = {}

        with open("weather.csv", 'r') as f:
            for i in f:
                temp = i.strip().split(";")
                self.dat[temp[1]] = [temp[2], temp[3]]

    @property
    def description(self):
        if self.w_dat:
            return self.w_dat['weather'][0]['description']

    @property
    def image(self):
        if self.w_dat:
            return 'http://openweathermap.org/img/w/{}.png'.format(self.w_dat['weather'][0]['icon'])

    def danger(self):
        return float(self.dat[self.description][-1])/50

    def weather_coord(self, coord):
        urll = "https://api.openweathermap.org/data/2.5/weather?lat="
        urll += str(coord['lat']) + "&lon=" + str(coord['lon']) + "&appid=" + api
        x = urllib.request.urlopen(urll)
        obj = json.loads(x.read())
        self.w_dat = obj
        # print(obj['weather'][0]['id'])
        return obj['weather'][0]['description'].capitalize()


# a = Weather()
# a.weather_coord(50.40, 30.45)
# print(a.danger())
# print(weather_coord(50.40, 30.45))
