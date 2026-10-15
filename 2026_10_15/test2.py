import numpy as np

a = np.arange(12).reshape(3, 4)
print(a.shape, a.strides, a.dtype)
print(a.T.shape, a.T.strides)
print(a.flags['C_CONTIGUOUS'], a.T.flags['C_CONTIGUOUS'])

b = a.reshape(4, 3)
b[0, 0] = 99
print(a[0, 0], np.shares_memory(a, b), b.base is a)

c = a[:, ::2]
print(c.strides, c.flags['C_CONTIGUOUS'])
c[:] = -1
print(a)