import csv

with open('bus_stop.csv', 'r', encoding='Windows-1251') as bus_stop:
    #fields = ["Name", "Street", "StationName"]
    reader = csv.DictReader(bus_stop, delimiter=';')
    streets = {}
    for row in reader:
        if row['Street'] in streets:
            streets[row['Street']] += 1 
        else:
            streets[row['Street']] = 1
res = sorted(streets.items(), key=lambda x:x[1], reverse=True)
print(res[:5])