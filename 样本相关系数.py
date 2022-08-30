import csv
from math import *

with open(file='2000~2008 年全国生活用水量.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 0:
            years = row
        else:
            water = row
years.remove(years[0])
water.remove(water[0])
years = [int(number) for number in years]
water = [int(number) for number in water]

water_average = 0
for number in water:
    water_average += number
water_average = water_average / len(water)

years_average = 0
for number in years:
    years_average += number
years_average = years_average / len(years)

temp1 = temp2 = temp3 = 0
for i in range(0, 9):
    temp1 += (years[i] - years_average) * (water[i] - water_average)
    temp2 += pow(years[i] - years_average, 2)
    temp3 += pow(water[i] - water_average, 2)
temp2 = sqrt(temp2)
temp3 = sqrt(temp3)
r = temp1 / (temp2 * temp3)
print(r)
