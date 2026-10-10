# comprehension, 제너레이터, `enumerate`, `zip`, `map`

값의 즉시 생성 / lazy 생성간의 차이를 비교해보자.

- comprehension: `[expresion for point in iterable if condition]` 과 같은 문법으로, 3개가 있다.
    - 위의 것이 list의 comprehension이고, 
    - dict(`{key: value for point in iterable if condition}`)
    - set({element for point in iterable if condition})
- iterable vs iterator: iterable은 `iter()`를 적용할 수 있는 객체(list, str, dict등)이고, iterator는 `next()`로 하나씩 꺼내서 쓰는 일회용 객체이다. 이는 C++ STL과 크게 다르지 않다. 모든 값을 소진하면 `StopIteration`이 발생하고, `for`는 이것을 받으면 조용히 종료한다.
- generator: iterator의 일종이다(따라서 모든 generator는 iterator지만 모든 iterator는 generator는 아니다). 값을 미리 생성하지 않고, 우선 다음 값 만큼을 계산하고 정지한다. 만드는 방법은:
    - (x * x for x in range(n))과 같은 comprehension과 비슷한 표현식.
    - 함수 내부의 `yield`문. 
- 이러한 특성한 generator의 값은 일회용이고, `len()`을 호출할 수 없다.
    - `TypeError: object of type 'generator' has no len()`
- 다만 지연평가가 가능한 `enumerate`, `zip`, `map`등은 문제가 없다. (`zip`은 짧은 쪽에서 stop)