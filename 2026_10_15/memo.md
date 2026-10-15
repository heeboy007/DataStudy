
# Numpy 1일차

- ndarray는 데이터 버퍼 + (dshape, shape, strides) 메타 정보이다. 
    - dtype은 datatype, 즉 column 1개의 해석방식
    - shape는 해당하는 array의 모양
    - strides는 몇 다음원소까지 몇바이트를 건너뛰어야하는가?를 저장한다.
- 슬라이싱(`a[::2]`, `a[1:3]`)과 `reshape`, `.T`는 같은 버퍼를 다른 shape, stride로 보는 view를 생성한다.
    - 한마디로 말해서 새로운 공간을 할당하지 않는다는 말이다.
- fancy indexing(`a[[0, 2]]`), boolean mask(`a[a > 3]`)는 반대로 copy가 된다. 
- 원소 연산(`a + b`, `a * 2`, `a > 3`)은 python루프가 되지 않고 c등을 활용해 vectorize되어 있다.
- dtype은 반대로 고정이기 때문에 오버플로도 실제로 에러없이 순환되게 되어있고, 정수와 실수가 섞이면 큰쪽으로 승격된다.
    - 내부적으로 c를 활용한 type을 실제로 쓴다고 생각하자.

