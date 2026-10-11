
# `*args/**kwargs`, 스코프, 클로저, 데코레이터

## 인자를 받는 쪽(packing)
- `*args`는 남는 위치 인자를 tuple로, `**kwargs`는 남는 키워드 인자를 dict로 모은다.
- def를 통해 함수를 정의할 때, `*`뒤에 오는 메개변수는 keyword-only이다.(이름을 붙여서만 전달 가능.)
- 순서: `def f(위치, 기본값, *args, keyword-only, **kwargs)`

## 인자를 넘기는 쪽 (unpacking)
- `f(*seq)`는 seq를 위치인자로, `f(**dict)`는 dict를 키워드 인자로 풀어 넘긴다. `zip(*pairs)`도 응용법.
- 대입에서도 `first, *rest = seq`로 같은 `*`를 쓸 수 있다. 

## 스코프(LEGB)
- 이름은 Local -> Enclosing -> Global -> Builtin 순으로 찾는다고 한다.
- 함수 안에 어딘가에 일단 대입이 있다면, 그것을 보고 local하다고 한다.(함수의 local 변수라는 의미) 이는 컴파일 시점에 결정하고, 대입 전에 읽으면 `UnboundLocalError`가 납니다.
- 바깥 함수의 변수를 다시 대입하려면 키워드 `nonlocal`, 전역이라면 `global`을 써야한다. 읽기를 하거나 mutable 객체의 append같은 건 당연히 이렇게 할 필요 없이 바로 쓰면 된다.

## 클로저
- 안쪽 합수가 바깥 함수의 변수를 붙잡고(?) 있다면, 바깥 함수가 끝난 뒤에도 그 변수 자체가 cell객체에 남아있다. 이러한 확인은 `fn.__closure__`,`fn.__code__.co_freevars`등으로 할 수 있다고 한다.

## 데코레이터
- `@d`같은 데코레이터가 있다고 해보자. `def f`를 뒤에 붙이는 것은 사실은 `f = d(f)`를 하겠다는 것이나 다름 없다. `f`함수가 *`d`*라는 데코레이터가 한번 처리한 함수가 되는 것 뿐이다.
- wrapper는 `*args, **kwargs`로 받아 원래 함수에 그래도 넘기는 것이 관용적인 방법이다. `functools.wraps`를 활용하면 이름과 docstring도 보존할 수 있다.

