from geopy import distance
import csv

with open('metro_stop.csv', 'r', encoding='utf-8') as metro:
    reader = csv.DictReader(metro, delimiter=',')
    position = {}
    for row in reader:
        if row['NameOfStation'] not in position:
            position[row['NameOfStation']] = (row['Longitude_WGS84'],row['Latitude_WGS84'])
#print(position)

with open('bus_stop.csv', 'r', encoding='Windows-1251') as bus_stop:
    reader = csv.DictReader(bus_stop, delimiter=';')
    station_pos = {}
    for row in reader:
        if row['StationName'] != 'StationName' and row['Longitude_WGS84'] != 'Longitude_WGS84' and row['Latitude_WGS84'] != 'Latitude_WGS84':
            if row['StationName'] not in station_pos:
                station_pos[row['StationName']] = (row['Longitude_WGS84'],row['Latitude_WGS84'])

metro_bus_stop = {}
for m, c in position.items():
    metro_bus_stop[m] = 0
    pos = position[m] # Коорддинаты
    for b, v in station_pos.items():
        stat_pos = station_pos[b]
        dist = float(distance.distance(pos, stat_pos).km)
        if dist <= 0.5:
            metro_bus_stop[m] += 1
        else:
            metro_bus_stop[m] = 0 
    print(metro_bus_stop)
# res = sorted(metro_bus_stop.items(), key=lambda x:x[1], reverse=True)
# print(res[:5])



# metro = {'Китай город': (37.6316766, 55.7573154)}
# bus_stop = {'Китай город': (37.63495029, 55.75415472)}
dist = distance.distance(position['Академическая'], station_pos['Метро Академическая (южн.)']).km
print(f'{dist:.3f} км')
# #print('расстояние от станции до остановки', dist)
# Stops = {}
# if dist < 500:
#     Stops['Китай город'] = 1

# print(Stops)