# python


import csv

with open('monster_game.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    my_level = input()  # уровень играка
    n =  # счетчик кол-ва монстров, которых можно победить
    while my_level != 'хватит':
        my_level = int(my_level)
        n = 0  # счетчик кол-ва монстров, которых можно победить
        for row in answer:
            if int(row[-2]) != 0 and int(row[-2]) < my_level:
                n += 1

        if n == 0:
            print("Вы очень слабы. Сходите и наберитесь опыта!")
            my_level = input()
        else:
            print(f'Вы сможете победить: {n} монстров')
            my_level = input()
