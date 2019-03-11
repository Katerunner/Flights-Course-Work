import weath_loc
import parsik
import pprint

print('---Module delay---')
import delay
print('---Module weath_loc---')
print(weath_loc.weather_coord(5, 14))
print('---Module parsik---')
pprint.pprint(parsik.parse(parsik.get_html("https://www.flightstats.com/v2/flight-tracker/route/FRA/KTW/?year=2019&month=3&date=10&hour=12")))