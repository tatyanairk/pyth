# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = 20
min_item = -100
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]

print(array)

i = 0
index = -1

while i < size:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(index+1, ':', array[index])