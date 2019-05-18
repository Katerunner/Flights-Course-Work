class AirportsNet:
    """Represents the net of the airports"""

    def __init__(self, name='default_net', filename='bin/airports.dat'):
        self.name = name
        self.airdat = []
        with open(filename, 'r', encoding='utf-8') as (f):
            for i in f.readlines():
                try:
                    country = i.strip().replace('"', '').split(',')[3]
                    city = i.strip().replace('"', '').split(',')[2]
                    code_3 = i.strip().replace('"', '').split(',')[4]
                    name = i.strip().replace('"', '').split(',')[1]
                    code_4 = i.strip().replace('"', '').split(',')[5]
                    if len(code_3) != 3 or len(code_4) != 4:
                        raise Exception
                    lat = float(i.strip().replace('"', '').split(',')[6])
                    lon = float(i.strip().replace('"', '').split(',')[7])
                    self.airdat.append(Airport(name, country, city, code_3, code_4, lat, lon))
                except:
                    pass

    def find_by_airname(self, aname):
        """Returns airport by name"""
        for i in self.airdat:
            if i.name == aname:
                return i

    def find_by_code(self, cod):
        """Returns airport by code"""
        for i in self.airdat:
            if i.code_3 == cod:
                return i


class Airport:
    """Represents airport"""

    def __init__(self, name, country, city, code_3, code_4, lat, lon):
        """Initialization"""
        self.name = name
        self.country = country
        self.city = city
        self.code_3 = code_3
        self.code_4 = code_4
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        """Checks if airports are equal"""
        if self.code_3 == other.code_3:
            return True
        else:
            return False
