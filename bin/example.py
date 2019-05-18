from bin.weather import *
from bin.parsik import *
from bin.coordinates import Corray
import pprint
print('---Module weather---')
a = Weather()
print(a.weather_coord(Corray(5, 14)))
print('---Module parsik---')
pprint.pprint(parse(get_html("https://www.flightstats.com/v2/flight-tracker/route/FRA/KTW/?year=2019&month=3&date=10&hour=12")))