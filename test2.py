# python


import csv

with open('monster_game.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while (reader[j]['opportunity']) < (key['opportunity']) and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
        count = 1
    for el in reader:
        print(
            f'{el["MonsterName"]} имеет возможность: {el["opportunity"]}, вероятность использования возможности равна {el["probability"]} .')
        count += 1
        if count == 4:
            break
