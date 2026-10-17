
# pandas - DataFrame
DataFrame은 numpy 배열의 묶음이다. 열 하나가 ndarray하나에 인덱스를 포함한 것이다.
- 숫자를 사용하는 column은 이전에 살펴본 배열과 다르지 않은 연속 메모리구조를 가지고 있다.(stride등...)
- 문자열을 사용하는 column의 경우, dtype이 `object`이고 파이썬 문자열 객체의 reference 배열이다.

이렇게 되면 문제가 문자열이 중복되는 경우가 많을 때 손해가 크다는 것은 알고 있을 것이다.
이를 푸는 pandas식의 해법은 `categroy` dtype이다. 뭐 R의 factor랑 비슷하다고 생각하면 된다.
값 종류를 저장하고 행마다 정수만 가지고 있으면 되기 때문에 `np.unique(return_inverse=True)`와 기본적으로 같은 발상이다.

`groupby`는 split, apply, combine이다. 
1. 키 열을 정수 코드로 바꾸고(factorize)
2. 코드별로 행을 모아 집계(aggregate)
3. 키를 인덱스로하는 Series/DataFrame으로 결과를 return

`analyze.py`에서 `Counter`등으로 누적하고 dict로 돌리던 일을 원큐로 할수 있다는 것...

우선 이런 pandas가 numpy와 제일 달리하는 철학은 인덱스 정렬이다. Series끼리의 연산은 위치가 아니라 인덱스 라벨로 맞춰지고,
한쪽에 그 인덱스라벨이 없으면 그냥 `NaN`이 되어버린다. numpy는 해당하는 축의 원소가 1일 경우에 브로드캐스팅이 되지만, 여기선 그럴 일이 없다.