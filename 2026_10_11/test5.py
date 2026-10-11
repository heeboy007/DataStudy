
def trace(fn):
    def wrapper(*args, **kwargs):
        print(f"호출: {fn.__name__}{args} {kwargs}")
        result = fn(*args, **kwargs)
        print(f"반환: {result}")
        return result
    return wrapper

@trace
def add(a, b=0):
    return a + b

print(add(1, b=2))
# 호출: add(1,) {'b': 2}
# 반환: 3
# 3
print(add.__name__)
# wrapper

def sub(a, b=0):
    return a - b
sub = trace(sub)

print(sub(5, 3))
# 호출: add(5,) {'b': 3}
# 반환: 2
# 2

from functools import wraps

def trace2(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(args, kwargs)
    return wrapper

@trace2
def mul(a, b):
    """곱셈"""
    return a * b

print(mul.__name__, mul.__doc__, mul.__wrapped__)
# mul, 곱셈, <function mul at 0x10561d120>