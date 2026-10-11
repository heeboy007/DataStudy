# 오답노트

## test1.py
```python
f(1, 10, 20, 30, c=3, x=9)
# 1 10 (20, 30) 3 4 {'x': 9}
# it's tupled

first, *rest = [1, 2, 3, 4]
*init, last = "abc"
print(first, rest, init, last)
# 1 [2, 3, 4] 'ab' 'c'
# 1 [2, 3, 4] ['a', 'b'] 'c'
# it's listed
```

# 정리
실험 2에서 `=`와 달리 `lst.append`가 가능한 이유는 대입은 refernece자체를 바꾸는 연산이고, `append`는 객체 내부 정보를 바꾸는 연산기이기 때문이다. `=`는 이미 해당하는 reference(이름)이 존재하지만 그 scope가 local이 아닐 때, UnboundLocalError를 낸다고 생각하면 될 것 같다. `nonlocal`, `global`은 그것을 scope체크를 override한다고 보면 되지 않을까 싶다.
 - claude의 보충 설명: "해당 이름이 존재하지만 scope가 local이 아닐 때"가 아니라 "그 이름이 local이라고 컴파일 시점에 이미 결정됐는데, 아직 값이 묶이기 전에 읽을 때" 납니다. 함수 본문 어디에든 대입이 있으면 그 이름은 함수 전체에서 local이 됩니다. 그래서 global x가 아예 없어도 같은 에러가 나고(NameError가 아닙니다), make_bad의 n += 1도 n = n + 1이라 local n을 읽다가 실패합니다. global/nonlocal은 검사를 끄는 게 아니라 "이 이름은 local이 아니라 바깥 것이다"라고 선언하는 것이고, 그래서 대입이 바깥 이름표를 옮기게 됩니다.

실험 4의 `fs`는 i에 해당하는 cell이 1개가 공유되는 것이고, `fs3`의 경우 `make`로 인해서 cell이 별도로 생겨서 실제로는 3개가 된다. 그래서 fs3는 어느정도 의도에 부합하게 움직인다.

```python
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
```
우선 decorator는 `f=d(f)`와 같다고 생각하면 해설하기 편하다. `@d`라고 적은 시점에서 이미 `d`는 함수를 받아 함수를 return하는 함수여야한다. `@timed(repeat=3)`처럼 데코레이터에 argument도 넣고 싶으면 아래에 실제 decorator를 return할 수 있게 2중 구조로 짜일 수 밖에 없다. 그래야`f = timed(repeat=1)(f)`, 풀어서 보면 `f = deco(f)`가 성립한다. 다만 실제 decorator안에 이미 정의된 decorator를 또 쓰고 싶으면 def를 다시 써야하니까, wrapper까지 등장해서 `@wraps(fn)`을 성립시켰다. 이렇게 하면 docstring이나 name들도 fn에서 받아서 계승시킬 수 있다.

# 오늘 처음 안 것
- `*args` 문법이 def에서 쓰일 경우 tuple, 그외에는 unpack에서는 우변의 context에 따라 달라진다.
    - 예를 들어 list를 unpack 하면 list, tuple이면 tuple, dict면 dict이고, str는 char를 한개씩 담은 list이다.
