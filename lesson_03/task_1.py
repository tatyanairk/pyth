# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

digits = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            digits[j-2] += 1
i = 0

while i < len(digits):
    print(i + 2, '-', digits[i])
    i += 1
