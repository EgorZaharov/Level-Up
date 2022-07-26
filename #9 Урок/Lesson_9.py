a = [1, 2, 3, 4, 5, 6]

b = a.index(max(a))
c = a.index(min(a))
a[b],a[c] = a[c],a[b]

print(a)

