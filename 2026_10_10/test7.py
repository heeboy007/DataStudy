
fs = [lambda: i for i in range(3)]
print([f() for f in fs])
# [2, 2, 2]

fs2 = [lambda i=i: i for i in range(3)]
print([f() for f in fs2])
# [0, 1, 2]
