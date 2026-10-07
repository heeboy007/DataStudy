
x = 10
y = x
y += 1
print(x, y)
# 10, 11
print(id(x) == id(y))
# False

s = "abc"
t = s
t += "d"
print(s, t)
# abc abcd

l1 = [1, 2]
l2 = l1
l2 += [3]
print(l1, l2)
# [1, 2, 3] [1, 2, 3]

# 4/4 correct