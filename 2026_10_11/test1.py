
def f(a, b=2, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)

f(1, c=3)
# 1 2 [] 3 4 {}
f(1, 10, 20, 30, c=3, x=9)
# 1 10 (20, 30) 3 4 {'x': 9}
# it's tupled

try:
    f(1, 2, 3)
except TypeError as e:
    print("에러:", e)
# c부터는 c = 3, 같이 keyword를 써야만 할당할 수 있음

def g(x, y, z):
    return x + y + z

print(g(*[1, 2, 3]), g(**{ 'x': 1, 'y': 2, 'z': 3 }), g(1, *[2, 3]))
# 6 6 6

a, b = {'x': 1}, {'y': 2, 'z': 3}
print(g(**a, **b))
# 6
print({**a, **b, 'x': 100})
# {'x': 100, 'y': 2, 'z': 3}

first, *rest = [1, 2, 3, 4]
*init, last = "abc"
print(first, rest, init, last)
# 1 [2, 3, 4] ['a', 'b'] 'c'
# 재미있게도 바깥의 *init, last = "abc"처럼 받는 것과 def로 받는 args는 다르다...

pairs = [(1, 'x'), (2, 'y'), (3, 'z')]
print(list(zip(*pairs)))
# [(1, 2, 3), ('x', 'y', 'z')]
