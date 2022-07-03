# Строки
# Задача А
# n = input()
# print(f"""Количество пробелов: {n.count(' ')}""")

# Задача Б - вариант 1
# n = input()
# x = n.split()
# for i in x:
#    print(i,end=' ')
# print(f".")

# Задача Б - вариант 2 (с условием окончания ввода пустой строки)
# n = list(iter(input, ''))
# for i in n:
#     print(i,end=' ')
# print(f".")

# Функции
# Задача А
# def three_digit(a, b, c):
#     if c == '+':
#         print(a + b)
#     elif c == '-':
#         print(a - b)
#     elif c == '/':
#         print(a / b)
#     elif c == '*':
#         print(a * b)
#     else:
#         print("Ошибка")
#
# a = int(input("Введите число:"))
# b = int(input("Введите число:"))
# c = input("Введите знак математической операции:")
# print(three_digit(a, b, c))

# Задача Б
# def three_digit(a, b, c):
#     k=a
#     for i in range(1, b+1, 1):
#         k = k + k * c / 100
#     print(k)
#
#
# n = int(input("Размер вклада, руб.:"))
# m = int(input("Срок вклада, лет:"))
# l = int(input("Процентная ставка, %:"))
# print(three_digit(n, m, l))

# Домашняя работа
# Задача 1
# a = input().split()
# l = []
# for i in range(len(a)):
#     l.append(a[i])
#
# l = list(map(int,l))
# m = []
# for j in range(len(l)):
#     if l[j] % 3 == 0 and l[j] %5 != 0:
#         m.append(l[j])
# m = set(m)
# print(f"Максимальное значение: {max(l)}; Минимальное значение: {min(l)}; Все числа делящиеся на 3, но неделящиеся на 5: {sorted(m)}")

# Домашняя работа
# Задача 2

a = input().split()
l = []
for i in range(len(a)):
    l.append(a[i])
l = list(map(int,l))

for j in l:
    if l.count(j) == 1:
        print(j)