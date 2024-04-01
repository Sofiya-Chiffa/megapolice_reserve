# Python

import csv

# открытие файла
with open("transactions.txt", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter="?"))[1:]
    # создание переменных для хранения новой таблицы и минимальной цены товара
    answer = []
    min_cost = ["", 10 ** 5]
    # отбор нужных строк таблицы и поиск минимальной цены
    for line in r:
        if "набор" in line[4].lower():
            answer.append([line[4], line[6]])
            if float(line[6].replace(",", ".")) < min_cost[1]:
                min_cost = [line[4], float(line[6].replace(",", "."))]
    # создание нового файла
    with open("pack.csv", "w", newline="", encoding="utf8") as newf:
        w = csv.writer(newf, delimiter="?")
        w.writerow(["ItemDescription", "CostPerItem"])
        w.writerows(answer)
    # вывод ответа
    print(f"Самый дешевый товар в категории набор: {min_cost[0]}, цена такого товара составит: {min_cost[1]}")
