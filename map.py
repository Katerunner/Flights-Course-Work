# from geopy.geocoders import Nominatim
# from tqdm import tqdm
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# from geopy.extra.rate_limiter import RateLimiter
# geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
import random
import folium
import weather
import airports
from coordinates import Corray
import math


def distance_on_unit_sphere(coord1, coord2):
    """Returns length between 2 coordinates"""
    lat1 = coord1['lat']
    long1 = coord1['lon']
    lat2 = coord2['lat']
    long2 = coord2['lon']
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    # theta = longitude
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) =
    # sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    return round(arc * 6373, 1)


def update_map(c_dep, c_arr):
    """Updates the map"""
    dep = airports.AirportsNet().find_by_code(c_dep)
    dep_c = Corray(dep.lat, dep.lon)
    dep_w = weather.Weather()
    dep_w.weather_coord(dep_c)
    arr = airports.AirportsNet().find_by_code(c_arr)
    arr_c = Corray(arr.lat, arr.lon)
    arr_w = weather.Weather()
    arr_w.weather_coord(arr_c)

    map = folium.Map(tiles='Mapbox Control Room', attr='Thank you', location=[dep.lat, dep.lon], zoom_start=3)

    folium.TileLayer('Mapbox Bright', attr='Thank you', name="Mapbox Bright").add_to(map)
    # folium.TileLayer('Mapbox Control Room', attr = 'Thank you', name = "Mapbox Control Room").add_to(map)
    folium.TileLayer('stamenterrain', attr='Thank you', name="Stamen Terrain").add_to(map)
    folium.TileLayer('stamentoner', attr='Thank you', name="Stamen Toner").add_to(map)
    folium.TileLayer('stamenwatercolor', attr='Thank you', name="Stamen Water Color").add_to(map)
    folium.TileLayer('cartodbpositron', attr='Thank you', name="Cartodbpositron").add_to(map)
    folium.TileLayer('cartodbdark_matter', attr='Thank you', name="Cartodbdark Matter").add_to(map)

    ap_group = folium.FeatureGroup(name="Airports name")
    # we_group = folium.FeatureGroup(name="Airports weather")
    map.add_child(ap_group)
    # map.add_child(we_group)
    map.add_child(folium.LayerControl())

    icon_dep = folium.features.CustomIcon(dep_w.image, icon_size=(40, 40))
    icon_arr = folium.features.CustomIcon(arr_w.image, icon_size=(40, 40))
    icon_info = folium.features.CustomIcon(
        "https://www.forestgrove-or.gov/sites/default/files/imageattachments/community/page/3441/information-icon-29.png",
        icon_size=(20, 20))

    # folium.Marker([43, -79],
    #               popup='Iron Man',
    #               icon=icon
    #               ).add_to(map)

    pop_dep = dep.name + "<br><br>City: " + dep.city + "<br>Country: " + dep.country + "<br>Weather: " + dep_w.description.capitalize()
    ap_group.add_child(folium.Marker(location=[dep.lat, dep.lon], popup=pop_dep, icon=icon_dep))

    pop_arr = arr.name + "<br><br>City: " + arr.city + "<br>Country: " + arr.country + "<br>Weather: " + arr_w.description.capitalize()
    ap_group.add_child(folium.Marker(location=[arr.lat, arr.lon], popup=pop_arr, icon=icon_arr))

    pop_len = "Distance: " + str(distance_on_unit_sphere(dep_c, arr_c)) + " km"
    ap_group.add_child(folium.Marker(
        icon=icon_info, location=[(arr_c['lat'] + dep_c['lat']) / 2, (arr_c['lon'] + dep_c['lon']) / 2], popup=pop_len))

    folium.PolyLine(locations=[[dep_c['lat'], dep_c['lon']], [arr_c['lat'], arr_c['lon']]], color='red', weight=5, opacity=0.3).add_to(map)

    # with open('airports.dat', 'r', encoding='utf-8') as f:
    #     for i in f:
    #         try:
    #             lat = float(i.strip().split(",")[6])
    #             lon = float(i.strip().split(",")[7])
    #             pop = (str(i.strip().split(",")[2]) + ", " + str(i.strip().split(",")[3]) + ", " + str(
    #                 i.strip().split(",")[5])).replace('"', "").replace('"', "")
    #             pop_we = str(i.strip().split(",")[2]) + ", " + weather.weather_coord(lat, lon)
    #             # pop = pop.encode(encoding='UTF-8',errors='xmlcharrefreplace')
    #             print(i.strip().split(",")[0])
    #             ap_group.add_child(folium.Circle(radius=110, location=[lat, lon], popup=pop, fill=False, color='red'))
    #             we_group.add_child(
    #                 folium.Circle(radius=150, location=[lat, lon], popup=pop_we, fill=False, color='blue'))
    #             if int(i.strip().split(",")[0]) % 20 == 0:
    #                 map.save("map.html")
    #                 print('suc')
    #         except:
    #             print('err')
    #     folium.PolyLine(locations=[[-5.826789855957031, 144.29600524902344], [64.04309844970703, -139.1280059814453]],
    #                     color='gray', weight=1, opacity=0.3).add_to(map)
    map.save("map.html")

# update_map("FRA", "IEV")
