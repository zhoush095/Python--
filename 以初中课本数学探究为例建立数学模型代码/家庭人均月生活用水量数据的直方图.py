import csv
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["savefig.dpi"] = 1200
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

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

plt.title(title)
plt.hist(water, bins=range(3, 8))
plt.yticks(range(0, 11))
plt.xlabel('用水区间')
plt.ylabel('用水量')
plt.show()
