# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите любое натуральное число: '))
s = 0

for i in range(1, n+1):
    s += i

p = n * (n + 1) // 2

if s == p:
	print('{} = {}. Равенство выполнилось!'.format(s, p))

else:
	print('{} != {}. Равенство не выполнилось :('.format(s, p))