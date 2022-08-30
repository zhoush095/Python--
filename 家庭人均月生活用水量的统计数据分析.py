import csv


with open(file='家庭人均月生活用水量的统计调查.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    water = []
    for index, row in enumerate(reader):
        if index != 0:
            water.append(float(row[0]))
        else:
            water.append(row[0])
title = water[0]
water.remove(water[0])
a = b = c = 0
for i in range(0, 30):
    if 3.6 <= water[i] <= 5.4:
        a += 1
    elif water[i] <= 3.6:
        b += 1
    else:
        c += 1
print(a)
print(b)
print(c)
x = 0
for i in range(0, 30):
    x += water[i]
x /= len(water)
print(x)
