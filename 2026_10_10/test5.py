import sys, tracemalloc

N = 1_000_000
lst = [i * i for i in range(N)]
gen = (i * i for i in range(N))

print(sys.getsizeof(lst), sys.getsizeof(gen))
# former should be way higher, since list comprehension is makind the entire list.
# but getsizeof will evaluate only the list or the generator ifself, not it's containment.
# so it looks almost identical

def peak_mb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1e6

print(f"list 방식:       {peak_mb(lambda: sum([i * 1 for i in range(N)])):.1f}MB")
print(f"generator 방식:  {peak_mb(lambda: sum((i * 1 for i in range(N)))):.3f}MB")