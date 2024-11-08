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
a = b = c = 0
for i in range(0, 30):
    if 3.6 <= water[i] <= 5.4:
        a += 1
    elif water[i] <= 3.6:
        b += 1
    else:
        c += 1
water = np.array([a / 100, b / 100, c / 100])
plt.pie(water, labels=['比平均标准低', '处于平均标准', '比平均标准高'], colors=["#d5655d", "#5d1ca2", "#45a476"], autopct='%.2f%%',
        textprops={'fontsize': 10})
plt.title("家庭人均月生活用水量的数据扇形图")
plt.show()
