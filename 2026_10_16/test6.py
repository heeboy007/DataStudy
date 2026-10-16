import numpy as np

rng = np.random.default_rng(0)

users = rng.integers(0, 5, size=100_000)
actions = rng.integers(0, 4, size=100_000)
table = np.zeros((5, 4), dtype=np.int64)
np.add.at(table, (users, actions), 1)

print(table, table.sum())