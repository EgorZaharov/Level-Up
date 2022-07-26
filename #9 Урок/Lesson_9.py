# #Task 1
# a = [1, 2, 3, 4, 5, 6]
#
# b = a.index(max(a))
# c = a.index(min(a))
# a[b],a[c] = a[c],a[b]
#
# print(a)

# Task 2

def isSublist(x, y):
    if set(y) <= set (x):
        return True
    else:
        return False

x = list(input())
y = list(input())
a = isSublist(x, y)
print(a)


