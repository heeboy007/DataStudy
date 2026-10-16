
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(loc=[10, 100, 1000], scale=[1, 10, 100], size=(10_000, 3))
Z = (X - X.mean(axis=0)) / X.std(axis=0)
print(Z.mean(axis=0).round(6), Z.std(axis=0).round(6))

v = np.arange(3)
print(v[:, None].shape, v[None, :].shape, v[:, np.newaxis, None].shape)