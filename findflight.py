airports = {}
import pprint

with open('airports.dat', 'r', encoding = 'utf-8') as f:
    for i in f:
        country = i.strip().replace('"', "").split(",")[3]
        code_3 = i.strip().replace('"', "").split(",")[4]
        airport = {i.strip().replace('"', "").split(",")[1]: code_3}
        code_4 = i.strip().replace('"', "").split(",")[5]
        if country not in airports:
            if code_3 != '\\N' and len(code_3) == 3:
                airports[country] = [airport]
        else:
            if code_3 != '\\N' and len(code_3) == 3:
                airports[country] += [airport]
    # pprint.pprint(airports)