
import time
import numpy as np

N = 2_000_000
lst = list(range(N))
arr = np.arange(N, dtype=np.int64)

t = time.perf_counter()
s1 = sum(x * x for x in lst)
t_py = time.perf_counter() - t

t = time.perf_counter()
s2 = int((arr * arr).sum())
t_np = time.perf_counter() - t

print(s1 == s2, f"python: {t_py:.3f}s numpy: {t_np:.3f}s x{t_py/t_np:.0f}")

