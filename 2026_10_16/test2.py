
import numpy as np

b = np.broadcast_to(np.arange(3), (1000, 3))
print(b.shape, b.strides, b.nbytes)
print(b.flags['WRITEABLE'], b.base is not None)

try:
    b[0, 0] = 1
except ValueError as e:
    print("에러:", e)

