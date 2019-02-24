# from geopy.geocoders import Nominatim
# from tqdm import tqdm
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# from geopy.extra.rate_limiter import RateLimiter
# geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
import random
import folium
import weath_loc



map = folium.Map(tiles ='Mapbox Control Room', attr = 'Thank you')

folium.TileLayer('Mapbox Bright', attr = 'Thank you', name = "Mapbox Bright").add_to(map)
# folium.TileLayer('Mapbox Control Room', attr = 'Thank you', name = "Mapbox Control Room").add_to(map)
folium.TileLayer('stamenterrain', attr = 'Thank you', name = "Stamen Terrain").add_to(map)
folium.TileLayer('stamentoner', attr = 'Thank you', name = "Stamen Toner").add_to(map)
folium.TileLayer('stamenwatercolor', attr = 'Thank you', name = "Stamen Water Color").add_to(map)
folium.TileLayer('cartodbpositron', attr = 'Thank you', name = "Cartodbpositron").add_to(map)
folium.TileLayer('cartodbdark_matter', attr = 'Thank you', name = "Cartodbdark Matter").add_to(map)

ap_group = folium.FeatureGroup(name="Airports name")
we_group = folium.FeatureGroup(name="Airports weather")
map.add_child(ap_group)
map.add_child(we_group)
map.add_child(folium.LayerControl())

with open('airports.dat', 'r', encoding = 'utf-8') as f:
    for i in f:
        try:
            lat = float(i.strip().split(",")[6])
            lon = float(i.strip().split(",")[7])
            pop = (str(i.strip().split(",")[2]) + ", " + str(i.strip().split(",")[3]) + ", " + str(i.strip().split(",")[5])).replace('"',"").replace('"',"")
            pop_we = str(i.strip().split(",")[2]) + ", " + weath_loc.weather_coord(lat,lon)
            # pop = pop.encode(encoding='UTF-8',errors='xmlcharrefreplace')
            print(i.strip().split(",")[0])
            ap_group.add_child(folium.Circle(radius=110, location = [lat, lon], popup=pop, fill=False, color = 'red'))
            we_group.add_child(folium.Circle(radius=150, location = [lat, lon], popup=pop_we, fill=False, color = 'blue'))
            if int(i.strip().split(",")[0]) % 20 == 0:
                map.save("map.html")
                print('suc')
        except:
            print('err')
    folium.PolyLine(locations=[[-5.826789855957031,144.29600524902344], [64.04309844970703,-139.1280059814453]], color='gray', weight=1, opacity=0.3).add_to(map)
    map.save("map.html")
