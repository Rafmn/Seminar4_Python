# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

k = int(input('Введите натуральную степень: '))
import random
list = ''
for i in range(k, -1, -1):
    n = random.randint(0, 100)
    if i > 1:
        list += str(n) + '*x' + '^' + str(i)
        list += '+'
    elif i > 0:
        list += str(n) + 'x'
        list += '+'
    else:
        list += str(n)
list += '=0'
text = open('file.txt', 'w')
text.write(list)
text.close()
