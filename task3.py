# Python

import csv

# открытие файла
with open("transactions.txt", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter="?"))[1:]
    # создание словаря для облегчения поиска
    goods = {}
    for line in r:
        goods[line[3]] = line
    # цикл консольной программы
    while True:
        # ввод пользователя
        user = input()
        # выход из программы
        if user == "none":
            break
        # ответы на запрос пользователя
        if user in goods.keys():
            print(f"По вашему запросу: {user} найден следующий вариант:")
            print(" ".join(goods[user]))
        else:
            print("такого товара в базе нет")
