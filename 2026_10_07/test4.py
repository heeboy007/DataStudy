import copy

grid = [[0, 0], [0, 0]]
row_copy = grid.copy()
row_copy[0][0] = 7
print(grid)
# [[7, 0], [0, 0]]

deep = copy.deepcopy(grid)
deep[1][1] = 9
print(grid, deep)
# [[7, 0], [0, 0]] [[7, 0], [0, 9]]

bad = [[0] * 2] * 3
bad[0][0] = 1
print(bad)
# [[1, 0], [1, 0], [1, 0]]

# 3/3 correct