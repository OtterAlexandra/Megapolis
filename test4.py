# python


import csv

with open('monster_game.csv', encoding="utf8") as csvfile:
    classes = {}

    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    for row in answer:
        if row[0].split()[1] not in classes:
            classes[row[0].split()[1]] = {'count': 0, 'summa': 0}
            classes[row[0].split()[1]]['count'] += 1
            classes[row[0].split()[1]]['summa'] += int(row[-4])

        else:
            classes[row[0].split()[1]]['count'] += 1
            classes[row[0].split()[1]]['summa'] += int(row[-4])

for i in classes:
    count = classes[i]['count']
    sr = classes[i]['summa'] / classes[i]['count']
    print(f'{count} монстров класса {i}, средняя сила атаки {sr}')
