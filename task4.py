# Python

import csv

# открытие файла
with open("transactions.txt", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter="?"))[1:]
    # создание словаря для определения суммы покупок для каждого покупателя
    buyers = dict()
    m = 0
    for line in r:
        buyers.setdefault(line[0], 0)
        buyers[line[0]] += float(line[6].replace(",", "."))
    # сортировка по убыванию
    answer = []
    for key in buyers.keys():
        answer.append([buyers[key], key])
    answer.sort(reverse=True)
    # создание нового файла
    with open("best_buyer.csv", "w", newline="", encoding="utf8") as newf:
        w = csv.writer(newf, delimiter="?")
        w.writerow(["user id", "сумма покупок"])
        for b in answer[:7]:
            w.writerow([b[1], b[0]])
