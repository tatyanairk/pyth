# Определить, какое число в массиве встречается чаще всего.

import random

size = 10
min_item = 1
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]

print(array)

num = array[0]
max_frq = 1

for i in range(size-1):
    frq = 1
    for j in range(i+1, size):
        if array[i] == array[j]:
            frq +=1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(max_frq, 'раз встречается число', num)
else:
    print('Все элементы уникальны')