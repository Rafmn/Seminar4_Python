# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

text1 = open('file1.txt', 'w')  # Создание первого файла с многочленом
text1.write('2x² + 4x + 5 = 0')
text1.close()

text2 = open('file2.txt', 'w')  # Создание второго файла с многочленом
text2.write('3x² + 6x + 1 = 0')
text2.close()

text_1 = open('file1.txt', 'r') # Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
line1 = text_1.read().split('+')
line1 = [i.lstrip() for i in line1]
text1.close()

text_2 = open('file2.txt', 'r') # Считывание с файла и создание списка с раздением по знаку "+" и удаление первых пробелов
line2 = text_2.read().split('+')
line2 = [i.lstrip() for i in line2]
text2.close()

line1 = [int(i[0]) for i in line1]
line2 = [int(i[0]) for i in line2]

line3 = []
for i in range(3):                        # Суммирование коэффициентов многочлена
    line3.append(line1[i] + line2[i]) 

list = str(line3[0]) + 'x²' + '+' + str(line3[1]) + '+' + str(line3[2])  + '=0' # Создание окончательного текста многочлена


text3 = open('file3.txt', 'w')  # Запись полученного текста в файл
text3.write(list)
text3.close()