
import sys, tracemalloc
import numpy as np

N = 1_000_000

tracemalloc.start()
lst = list(range(N))
cur_list, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
arr = np.arange(N, dtype=np.int64)
cur_arr, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()

v = arr[:] #view

print(f"list: {cur_list/1e6:.1f}MB / ndarray {cur_arr/1e6:.1f}MB")
print(arr.dtype, arr.itemsize, arr.nbytes)
print(sys.getsizeof(v), sys.getsizeof(arr)) # the view VS array itself
print(np.arange(N, dtype=np.int8).nbytes)

# list: 40.0MB / ndarray 8.0MB
# int64 8 8000000
# 8000112 8000112
# 1000000