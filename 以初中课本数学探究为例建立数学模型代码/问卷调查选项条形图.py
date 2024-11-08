import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["savefig.dpi"] = 1200
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

with open(file='家庭人均月生活用水量的统计调查.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    X = []
    Y = []
    Z = []
    for index, row in enumerate(reader):
        if index != 0:
            X.append(row[1])
            Y.append(row[2])
            Z.append(row[3])
plt.subplot(2, 2, 1)
plt.bar(["A", "B", "C", "D"], [X.count("A"), X.count("B"), X.count("C"), X.count("D")])
plt.xlabel('问题1选项')
plt.ylabel('人数')
plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C", "D"], [Y.count("A"), Y.count("B"), Y.count("C"), Y.count("D")])
plt.xlabel('问题2选项')
plt.ylabel('人数')
plt.subplot(2, 2, 3)
plt.bar(["A", "B", "C", "D"], [Z.count("A"), Z.count("B"), Z.count("C"), Z.count("D")])
plt.xlabel('问题3选项')
plt.ylabel('人数')
plt.suptitle("问卷调查选项条形图")
plt.subplots_adjust(hspace=0.3)
plt.show()
