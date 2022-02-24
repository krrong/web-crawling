import csv

file = open('example.csv', 'r', encoding='utf-8')
placeLists = list()
reader = csv.reader(file)

for line in reader:
    place = line[3]
    placeLists.append(place)
file.close()

print(placeLists)