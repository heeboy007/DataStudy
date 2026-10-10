
names = ['a', 'b', 'c']
scores = [90, 80]

print(list(enumerate(names, start=1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]

print(list(zip(names, scores)))
# [('a', 90), ('b', 80)]

try:
    list(zip(names, scores, strict=True))
except ValueError as e:
    print("에러:", e)

m = map(str.upper, names)
print(m)
# generator?
# (map object)
print(list(m))
# ['A', 'B', 'C']
print(list(m))
# []

pairs = [(1, 'x'), (2, 'y'), (3, 'z')]
nums, chars = zip(*pairs)
print(nums, chars)
# (1, 2, 3,), ('x', 'y', 'z')
print(dict(zip(names, scores)))
# { 'a': 90, 'b': 80 }