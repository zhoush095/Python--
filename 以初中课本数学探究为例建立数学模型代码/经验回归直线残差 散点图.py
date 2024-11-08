import csv
from math import *
import matplotlib.pylab as plt

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
water.remove(water[0])
water = [int(number) for number in water]
water_average = 0
for number in water:
    water_average += number
water_average = water_average / len(water)
years.remove(years[0])
years = [int(number) for number in years]
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
years_linear_regression_equation = 1999
C = [0] * 9
for i in range(0, 8):
    years_linear_regression_equation += 1
    C[i] = water[i] - b * years_linear_regression_equation - a
plt.xlabel("年份")
plt.ylabel("残差")
plt.scatter(years, C)
plt.grid(axis='y')
plt.show()
