class V:
    def __init__(self, x, y):
        self.x, self.y = x, y

a, b = V(1, 2), V(1, 2)
print(a == b, a is b)
# False False
print(a)
# <class P at 0xwtf>
print(len({a, b}))
# 2

class V2(V):
    def __repr__(self):
        return f"V2({self.x}, {self.y})"
    def __eq__(self, o):
        return isinstance(o, V2) and (self.x, self.y) == (o.x, o.y)

c, d = V2(1, 2), V2(1, 2)

print(c == d, c, [c])
# True <class P at 0xwtf> [V2(1, 2)]
print(V2.__hash__)
# None

try:
    {c}
except TypeError as e:
    print("에러: ", e)


class V3(V2):
    def __hash__(self):
        return hash((self.x, self.y))

k = V3(1, 2)
s = {k}
print(V3(1, 2) in s)
# True
k.x = 99
print(V3(1, 2) in s, k in s)
# False False
# Reason: 확실하게는 모르겠지만, hash, eq간의 계약과 관련 있을 수는 있다.
# s가 k에 대한 reference와 함께 hash(k)의 값만 가지고 있고, 
# hash통해 검색한 이후에 eq까지 검사하는 구조라고 가정한다면 저런 behavior가 나올 법도 하다는 생각이다.
# 바뀌기 전의 k를 k1, 후를 k2로 두면, s = { hash(k1) -> k2 }와 같은 상태이다.
# hash(V3(1, 2)) == hash(k1)이긴 하지만 V3(1, 2) != k2이므로 전의 것이 False,
# hash(k2) != hash(k1) 이기 때문에 k2 == k2이더라도 후의 것이 False, 인것은 아닐지?
