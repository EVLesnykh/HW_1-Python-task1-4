# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input('Введите первый член арифметической прогрессии a1: '))
d = int(input('Введите разность арифметической прогрессии d: '))
n = int(input('Введите число членов последовательности n: '))
for i in range(n):
  print(a1 + i * d, end = ' ')