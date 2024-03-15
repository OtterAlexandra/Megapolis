# python


import csv

maxi = 0
with open('monster_game.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    result = []
    for row in answer:
        power = 0
        if row[1] == 'регенерация':
            power = int(row[-2]) * int(row[2])
            maxi = max(maxi, power)
        elif row[1] == 'дополнительный ход':
            power = int(row[2]) * (int(row[-1]) + int(row[-2]) + int(row[-3]) + int(row[-4]) + int(row[-5]))
        else:
            power = int(row[2]) * int(row[-4])
        result.append([row[1], power])

with open('monster_opportunity.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['opportunity', 'power'])
    w.writerows(result)

print('Регенерация: ' + str(power))

