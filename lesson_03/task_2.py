# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import random

size = 10
array = [0] * size
even = []

for i in range(size):
    array[i] = int(random() * 10) + 10
    if array[i] % 2 == 0:
        even.append(i)

print(array)
print('Индексы четных элементов: ', even)