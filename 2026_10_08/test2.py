
print(hash((1, 2)))
try:
    hash((1, [2]))
except TypeError as e:
    print("에러:", e)
# 그 안에 list가 있으니까

d = {}
d[1] = 'int'
d[1.0] = 'float'
d[True] = 'bool'
print(d, len(d))
# { 1: 'int', 1.0: 'flat', True: 'bool' } 3
print({1, 1.0, True, '1'})
# { 1, 1.0, True, '1' } 
# 순서는 달라질 수 있음.

d2 = {(1, 2): 'a'}
print(d2[(1, 2)])
# a