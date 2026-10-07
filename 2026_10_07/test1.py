
a = [1, 2, 3]
b = a
b.append(4)

print(a)
# [1, 2, 3, 4]
print(a is b)
# True
print(id(a), id(b))
# would be the same

c = a.copy()
c.append(5)
print(a, c)
# [1, 2, 3, 4] [1, 2, 3, 4, 5]
print(a == c, a is c)
# False False

# 5/5 correct