
import numpy as np
import tracemalloc

rng = np.random.default_rng(0)

tracemalloc.start()
P = rng.random((5000, 2))
D = np.sqrt(((P[:, None, :] - P[None, :, :]) ** 2).sum(axis=-1))
print(D.shape, np.allclose(D, D.T), np.diag(D))
c_size, peak_size = tracemalloc.get_traced_memory()
print(c_size, peak_size, D.nbytes)
tracemalloc.stop()

D2 = np.array([[np.linalg.norm(p - q) for q in P] for p in P])
print(np.allclose(D, D2))