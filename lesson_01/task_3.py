# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input("Введите номер буквы в алфавите "))

a = ord('a') + a - 1

print("Это буква", chr(a))