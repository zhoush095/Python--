import matplotlib.pyplot as plt
import csv

plt.rcParams["savefig.dpi"] = 1200
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

with open(file='2000~2008 年全国生活用水量.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            years = row
        else:
            water = row
plt.xlabel(years[0])
plt.ylabel(water[0])
years.remove(years[0])
water.remove(water[0])
years = [int(number) for number in years]
water = [int(number) for number in water]
plt.plot(years, water)
plt.show()
