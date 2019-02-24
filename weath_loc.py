import json
import requests
import urllib.request


def weather_coord(lat,lon):
    urll = "https://api.openweathermap.org/data/2.5/weather?lat="
    urll += str(lat) + "&lon=" + str(lon) + "&appid=" + api
    x = urllib.request.urlopen(urll)
    obj = json.loads(x.read())
    return obj['weather'][0]['description'].capitalize()

weather_coord(5, 14)