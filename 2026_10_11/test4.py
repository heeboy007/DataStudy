
fs = [lambda: i for i in range(3)]
print([f() for f in fs])
# [2, 2, 2]
print(fs[0].__closure__[0] is fs[1].__closure__[0]) #같은 객체냐고
# True
print(fs[0].__closure__[0].cell_contents)
# 2

fs2 = [lambda i=i: i for i in range(3)]
print(fs2[0].__closure__, fs2[0].__defaults__)
# None (0, )

def make(i):
    return lambda: i

fs3 = [make(i) for i in range(3)]
print([f() for f in fs3])
# [0, 1, 2]
print(fs3[0].__closure__[0] is fs3[1].__closure__[0]) #같은 객체냐고
# False