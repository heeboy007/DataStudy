
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c1, c2 = make_counter(), make_counter()
print(c1(), c1(), c1(), c2())
# 1 2 3 1

print(c1.__code__.co_freevars)
print(c1.__closure__[0].cell_contents)
# ('n', )
# 3

def make_bad():
    n = 0
    def inc():
        n += 1
        return n
    return inc

try:
    make_bad()()
except UnboundLocalError as e:
    print("에러:", e)
# 똑같이 현재 local에 존재하지 않는 변수에 쓰기를 시도(int는 불변이니까, 실제로는 쓰기 시도가 됨) 한것은 같다.
# 다만 시도한 범위의 실 변수가 global이었는지 closure였는지가 다를 뿐.

# 뭐 피하고 싶다면 단순히 가변객체를 활용해서 그 내부의 것을 변경하는 식으로 한다면 알아서 closure에 등록될 것이다.
def make_good():
    n_cont = { 'n': 0 }
    def inc():
        n_cont['n'] += 1
        return n_cont['n']
    return inc

c3 = make_good()
print(c3())