print([x * x for x in range(6)])
# [1, 4, 9, 16, 25, 36]

print([x for x in range(10) if x % 2 == 0])
# [2, 4, 6, 8, 10]

print(['even' if x % 2 == 0 else 'odd' for x in range(4)])
# ['even', 'odd', 'even', 'odd']

print([(i, j) for i in range(3) for j in range(i)])
# [(0, 0), (1, 0), (1, 1), (2, 0), (2, 0), (2, 2)]
# [(1, 0), (2, 0), (2, 1)]

matrix = [[1, 2, 3], [4, 5, 6]]
print([v for row in matrix for v in row])
# [1, 2, 3, 4, 5, 6]
print([[row[i] for row in matrix] for i in range(3)])
# [[1, 4], [2, 5], [3, 6]]
# transpose?

x = 'outer'
_ = [x for x in range(3)]
print(x)
# outer
good = [[0] * 2 for _ in range(3)]
bad = [[0] * 2] * 3
good[0][0] = 1
bad[0][0] = 1
print(good, bad)
# [[1, 0], [0, 0], [0, 0]] [[1, 0], [1, 0], [1, 0]]
