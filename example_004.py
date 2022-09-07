print('Введите координаты А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))
from math import sqrt
print('Дистанция между A и B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))