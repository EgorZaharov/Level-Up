# #Task 1
# a = [1, 2, 3, 4, 5, 6]
#
# b = a.index(max(a))
# c = a.index(min(a))
# a[b],a[c] = a[c],a[b]
#
# print(a)

# # Task 2
#
# def isSublist(x, y):
#     if set(y) <= set (x):
#         return True
#     else:
#         return False
#
# x = list(input())
# y = list(input())
# a = isSublist(x, y)
# print(a)

# Task 3 - Вараинт 1

# def my_set(x):
#     if len(x) <= 1:
#         yield x
#         yield []
#     else:
#         for i in my_set(x[1:]):
#             yield [x[0]]+i
#             yield i
#
# my_list = list(input().split())
# item = [x for x in my_set(my_list)]
#
# item.sort()
# print (item)

# Task 3 - Вараинт 2
# def all_subset(data):
#     subsets = [[]]
#     for i in range(len(data)):
#         for j in range(len(subsets)):
#             new_subset = subsets[j] + [data[i]]
#             subsets = subsets + [new_subset]
#     return subsets
#
# print (all_subset([1,2,3]))

# Словари
# Task 4 - Два списка
# a = list(input().split())
# b = list(input().split())
# my_dict = dict(zip(a, b))
#
# print(my_dict)

# Task 5 - Три списка

# student_ids = list(input("Введите ID студента:").split())
# student_names = list(input("Введите имя студента:").split())
# student_grades = list(input("Введите бал студента:").split())
#
# students = []
#
# for i in range(len(student_ids)):
#     my_dict = {student_ids[i]:{student_names[i]:student_grades[i]}}
#     students.append(my_dict)
#
# print(my_dict)

# Task Эрудит
my_dict = {
    1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2 : ['D', 'G'],
    3 : ['B', 'C', 'M', 'P'],
    4 : ['F', 'H', 'V', 'W', 'Y'],
    5 : ['K'],
    8 : ['J', 'X'],
    10 : ['Q', 'Z']
}

scrabble = input("Введите слово:")
scrabble.upper()
scrabble_new = list(scrabble.upper())
x = []
for n in my_dict:
    for i in scrabble_new:
        if i in my_dict[n]:
           x.append(n)

print(sum(x))