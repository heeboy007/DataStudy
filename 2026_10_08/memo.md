# `list`, `dict`, `set`의 내부 동작 모델과 선택 기준

- *list*는 동적인 배열이다. 인덱싱(`a[5]`등)은 O(1), `append`는 평균 O(1), `x in lst`등은 순회 연신이기 때문에 O(n), `insert`, `pop(0)`등은 전체를 다 밀어야해서 O(n)이다.
- *dict*, *set*은 해시 테이블이다. 따라서 키로 찾는 일(`k in d`, `x in s`)이 list와 대비해 평균 O(1)이다. 대신 키는 hashable이어야 하고, 보통 불변 객체가 그렇다. 
- hashable의 조건든 해시값이 객체 수명동안 변하지 않고, `==`와 일관적일것, 즉, hash를 `==`하나 그 객체 자를 `==`하나 같아야한다는 것.
    (그래서 `list`는 키가 될 수 없다.)
- dict는 Python 3.7부터 삽입순서를 보장하고, set은 그렇지 않다.
```python
a = dict()

a["apple"] = 1
a["banana"] = 2
a["cherry"] = 3

print(list(a.keys()))
# 이때 3.7미만이라면 구현에 따라 ["apple", "banana", "cherry"]가 아닌 값이 나올 수 있었음.
``` 
- 슬라이싱은 항상 새 객체를 얕은 복사를 통해서 만들고, 슬라이드 대입 / 삭제는 원본을 변경한다.
- `sorted()`는 새로운 list를 만들고, `.sort()`는 in-place하게 그 list를 정렬하고 `None`을 return한다. 이때 둘 다 stable하다.


