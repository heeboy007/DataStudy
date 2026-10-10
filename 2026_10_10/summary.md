
# 오답

```python
#test1.py range(i)인 시점에서 i=j인 시나리오는 없음
print([(i, j) for i in range(3) for j in range(i)])
# [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
# [(1, 0), (2, 0), (2, 1)]

#test2.py 순서가 다름
print(by_first)
# { 'b': 'Banana', 'c': 'cherry', 'a':'avocado' }
# {'a': 'avocado', 'b': 'Banana', 'c': 'cherry'}
print({ v: k for k, v in by_first.items() })
# { 'Banana': 'b', 'cherry': 'c', 'avocado': 'a' }
# {'avocado': 'a', 'Banana': 'b', 'cherry': 'c'}
```

## test5.py
```text
8448728 200
list 방식:       40.4MB
generator 방식:  0.000MB
```
생각보다 그렇게 까지 과소평가되진 않는듯하지만, peak mem은 10^4배 이상의 더 큰 차이가 존재


# 정리
실험 3에서 g2를 이용해서 list를 만들어도 소용 없는 이유는 이미 iterator가 Stopiteration, 즉 끝에 도달해서 더이상 순회할 element가 남아있지 않기 때문...
실험 5를 보면 굳이 값을 재사용 해야하거나 indexing(random access)등이 필요한게 아니라면 generator로 만들어 peak rss를 줄이는 것이 좋다.
실험 7의 경우, python이 그런 상황에서도 값을 참조하는 것이 허용하는게 좀 이상하다는 생각이다. 하여간에, lambda의 경우 expression으로 바로 evaluation 되는게 아니라 "i를 반환"한다는 제정이 되어서, i값이 마지막 range의 원소 2로 업데이트 된 상태에서 init가 종료, 차후에 부를 때 `[2, 2, 2]`가 되어 버린 것이다. fs2의 경우는 default값으로 i가 저장되어서 lambda 내외부의 i가 실질적으로는 다른것이라 `[0, 1, 2]`로 나오는 것으로 보인다.

# 처음 안 것
- 실험 5처럼 peak rss찍는 방법
- unzip하는 방법 `zip(*something)`, 그러나 정확한 기전은 모르겠음.