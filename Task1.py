d = input('Введите точность вычисления числа пи (формат ввода: 0.00001): ').split('.')
n = len(d[1])
import math
print('pi = ', round(math.pi, n))