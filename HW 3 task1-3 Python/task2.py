# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('Задайте размер массива N = '))
print("Введите элементы массива:")
array_N = []
for i in range(N):
  array_element = int(input(f'array_{i}-> '))
  array_N.append(array_element)
X = int(input('Введите число X = '))
element_array = 0
for i in range(len(array_N)):
    if (X - array_N[i]) < X - element_array and X - array_N[i] > 0:
        element_array = i
print(f'Близкий по величине к заданому числу Х = {X} элемент -> {array_N[element_array]}')