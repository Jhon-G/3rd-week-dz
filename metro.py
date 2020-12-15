import csv

with open('metro_stop.csv', 'r', encoding='utf-8') as metro:
    reader = csv.DictReader(metro, delimiter=',')
    station = {}
    for row in reader:
        #print(row['NameOfStation'], row['RepairOfEscalators'])
        if row['RepairOfEscalators'] != '': # If Value is empty string skip this name:
            if row['RepairOfEscalators'] in station:
                station[row['NameOfStation']] = row['RepairOfEscalators']
            else:
                station[row['NameOfStation']] = row['RepairOfEscalators']

for k , v in station.items():
    print('Идет ремонт эскалаторов:', k) 
