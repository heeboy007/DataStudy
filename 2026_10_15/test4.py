
import numpy as np

x = np.array([100, 100], dtype=np.int64)
print(x + x)

print(np.array([1, 2, 3]) / 2, (np.array([1, 2, 3]) / 2).dtype)
print((np.array([1, 2, 3], dtype=np.int8) + 1.5).dtype)

print(np.float32(0.1) + np.float32(0.2) == np.float32(0.3))
print(0.1 + 0.2 == 0.3, np.isclose(0.1 + 0.2, 0.3))

big = np.full(10_000_000, 0.1, dtype=np.float32)
print(big.sum(), big.sum(dtype=np.float64))


big2 = np.full(10_000_000, 0.1, dtype=np.float32)

print(float(big2.sum()))                       # pairwise (이미 본 값)
print(float(np.cumsum(big2)[-1]))              # 순차 누적, 마지막 원소
print(float(big2.sum(dtype=np.float64)))       # float64로 누적