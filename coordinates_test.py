from coordinates import *

a = Corray(1.56, 2.234)
print('Latitude:', a['lat'])
print('Longitude:', a['lon'])
a['lat'] = 21.5565
a['lon'] = -41.23456
print()
print('Length:', len(a))
print('Latitude:', a['lat'])
print('Longitude:', a['lon'])
