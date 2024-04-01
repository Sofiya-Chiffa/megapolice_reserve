# Python

import csv

# открытие файла
with open("transactions.txt", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter="?"))[1:]
    # создание словаря для хэширования
    months = dict()
    for line in r:
        m = int(line[2].split(".")[1])
        months.setdefault(m, [0, 0])
        months[m][0] += 1
        months[m][1] += float(line[6].replace(",", "."))
    # нахождение максимального кол-во покупок
    j = 0
    maxx = 0
    summ = 0
    for i in months.keys():
        if months[i][0] > maxx:
            j = i
            maxx = months[i][0]
            summ = months[i][1]
    # вывод ответа
    # print(j, maxx, summ / maxx)
    print(months)
