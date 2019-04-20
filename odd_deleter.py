with open("airlines_translator.csv", 'w') as o:
    with open("airlines.csv", 'r') as f:
        for i in f:
            line = i.strip().split(";")[:2]
            if line[0] != '' and line[1] != '':
                o.write(";".join(line) + "\n")