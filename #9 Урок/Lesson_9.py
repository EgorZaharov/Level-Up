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
a = list(input().split())
b = list(input().split())
my_dict = dict(zip(a, b))

print(my_dict)






