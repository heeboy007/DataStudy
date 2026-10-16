
import numpy as np

a = np.arange(6).reshape(2, 3)
print((a + np.array([10, 20, 30])).shape)
print((a + np.array([[10], [20]])).shape)

try:
    a + np.array([1, 2])
except ValueError as e:
    print("에러:", e)

x = np.arange(3).reshape(3, 1)
y = np.arange(4)

print((x + y).shape)
print(x + y)
# (3, 4)