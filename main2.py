# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

import random

n = int(input())
n_array = []

for i in range(n):
    n_array.append(random.randint(1, n))

print(n_array)

x = int(input())

nearest_value = n_array[0]
for i in n_array:
    if abs(i - x) < abs(nearest_value - x):
        nearest_value = i

print(f"ближе - {nearest_value}")