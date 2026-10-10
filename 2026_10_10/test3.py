
g = (x * x for x in range(3))
print(type(g))
# generator
print(next(g), next(g), next(g))
# 0 1 4
try: 
    next(g)
except StopIteration:
    print("바닥남")

g2 = (x * x for x in range(3))
print(list(g2))
# [0, 1, 4]
print(list(g2))
# []

lst = [1, 2, 3]
it = iter(lst)
print(next(it), next(it))
# 1 2
print(list(it))
# [3]
print(sum(x for x in range(5)))
# 10