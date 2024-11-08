import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.ticker import MultipleLocator

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
plt.scatter(years, water, s=7)

water_average = 0
for number in water:
    water_average += number
water_average = water_average / len(water)

years_average = 0
for number in years:
    years_average += number
years_average = years_average / len(years)

temp1 = temp2 = 0
for i in range(1,9):
    temp1 += (years[i] - years_average) * (water[i] - water_average)
    temp2 += pow(years[i] - years_average, 2)
b = temp1 / temp2
a = water_average - b * years_average

x = np.arange(2000, 2010)
Y = b * x + a
plt.plot(x, Y)
plt.xticks(np.linspace(2000, 2008, 9, endpoint=True))
plt.show()
