# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

import random
N = int(input())
X = int(input())
N_array = []
for i in range(N):
    N_array.append(random.randint(1 , 5))
    
print(N_array)
print(f' -  {N_array.count(X)}')