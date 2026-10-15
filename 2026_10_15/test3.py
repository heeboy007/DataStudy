import numpy as np

a = np.arange(6)
v = a[1:4]
v[0] = 100
print(a)

f = a[[1, 2, 3]]
f[0] = -5
print(a)

m = a[a > 2]
m[:] = 0
print(a)

a[a > 50] = 0
print(a)
print(np.shares_memory(a, a[1:4]), np.shares_memory(a, a[[1, 2, 3]]))