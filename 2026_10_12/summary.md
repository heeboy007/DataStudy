
# 오답노트

## test1
```python
print(a.__dict__, b.__dict__)
# { 'kind': 'wolf' } {}
# {'name': 'a', 'kind': 'wolf'} {'name': 'b'}
```

## test2
```python
p = P()
m = p.hi
print(m.__self__ is p, m.__func__ is P.hi)
# False True
```

# 정리
- 실험3의 마지막 줄의 경우, `hash(바뀌기 전 k)`를 활용해서 슬롯을 찾으므로 바뀐 객체로는 찾을 수 없다.
- 실험5의 경우는 `__iter__`가 지속적으로 갱신이 가능한 형태로 `c`가 만들어 졌으므로 `list(c)`는 계속 반복할 수 있다. 반대로 직접 iterator객체를 가져온 경우는 여전히 끝까지 값을 소진하면 다시 발급받을 수는 없으므로 다시 값을 추춣할 수 없게 된 것이다.
- 실험7에서 `@dataclass`가 기본으로는 가변객체임을 상정하고, 그럼 hash값 또한 evaluation시점에 따라 달라지게 되어버린다. 그럼 생존기간동안 hash값이 변하지 않아야하는 hashable의 정의에서 벗어나게 된다. `frozen=True`의 경우 반대로 이를 만족할 수 있다. `__eq__`와 `__hash__`의 계약으로 보면, `__hash__`가 실행되어 저장되었지만, frozen하지 않은 객체 x, y는 `hash(x) == hash(y)`이지만, `x != y`일 수도 있다.

# 오늘 알게 된것
- 인스턴스의 method가 실제로 function과 다른 종류의 객체이고 최종적으로 `Class.method(obj, args)`와 같은 형태로 처리된다는 것.