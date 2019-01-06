# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 10
min_item = 1
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(size)]

print(array)

mn = 0
mx = 0
for i in range(size):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i

print('position_min = {}; position_max = {}'.format(mn, mx))

summa = 0

for i in range(mn+1, mx):

    summa += array[i]

print('сумма элементов между максимальным и минимальным = ', summa)