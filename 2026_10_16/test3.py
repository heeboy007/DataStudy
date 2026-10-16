
import numpy as np

m = np.arange(12).reshape(3, 4)
print(m.sum(axis=0), m.sum(axis=1))
print(m.sum(axis=0).shape, m.sum(axis=1, keepdims=True).shape)
print(m - m.mean(axis=1, keepdims=True))
print((m - m.mean(axis=1, keepdims=True)).sum(axis=1))
