# Python

import csv

# открытие файла
with open("transactions.txt", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter="?"))[1:]
    line = 1
    n = r[line]
    # сортировка списка вставками
    while line < len(r):
        if line != 0 and n[4] > r[line - 1][4]:
            r[line] = r[line - 1]
            line -= 1
        else:
            r[line] = n
            line += 1
            if line < len(r):
                n = r[line]
    # ывод первых пяти значений
    for j in r[:5]:
        print(f"{j[1]} - {j[4]} - {j[6]}")
