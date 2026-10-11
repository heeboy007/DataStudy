import time
from functools import wraps

def timed(repeat=1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            t = time.perf_counter()
            for _ in range(repeat):
                r = fn(*args, **kwargs)
            ms = (time.perf_counter() - t) / repeat * 1000
            print(f"{fn.__name__}: {ms:.3f} ms/call")
            return r
        return wrapper
    return deco

@timed(repeat=3)
def slow(n):
    return sum(i * i for i in range(n))

print(slow(200_000))
# slow

def tag(name):
    def deco(fn):
        def w(*a, **k):
            return f"<{name}>{fn(*a, **k)}</{name}>"
        return w
    return deco

@tag("b")
@tag("i")
def hi():
    return "hi"

print(hi())
# <b><i>hi</i></b>