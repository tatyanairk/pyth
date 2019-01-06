# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

print('min[{}] = {}; max[{}] = {}'.format(mn+1, array[mn], mx+1, array[mx]))

b = array[mn]
array[mn] = array[mx]
array[mx] = b

for i in range(size):
    print(array[i], end = ' ')
print()



