import copy

a = [1, 2, [3, 4, 5]]
b = copy.copy(a)

print(a)
print(b)

a[2][1] = 100

print(a)
print(b)