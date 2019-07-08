import csv
import matplotlib.pyplot as plt

stations = {}

with open('metro-bike-share-trips-2019-q1.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for data in reader:
        if data['start_station'] not in stations:
            stations[data['start_station']] = {
                'start': 0,
                'end': 0,
                'total': 0
            }
        if data['end_station'] not in stations:
            stations[data['end_station']] = {
                'start': 0,
                'end': 0,
                'total': 0
            }
        stations[data['start_station']]['start'] += 1
        stations[data['start_station']]['total'] += 1
        stations[data['end_station']]['end'] += 1
        stations[data['end_station']]['total'] += 1

start_end_ratios = sorted(map(lambda s: (s[0], s[1]['end']/s[1]['start']),
                              stations.items()), key=lambda x: x[1])
station_list = sorted(stations.items(), key=lambda x: x[1]['total'])

# for ratio in start_end_ratios:
#     print(ratio)

plt.title('End / Start Ratio')
plt.plot([s[1] for s in start_end_ratios])
plt.show()
