
class P:
    def hi(self, x):
        return (self, x)

p = P()
m = p.hi
print(m.__self__ is p, m.__func__ is P.hi)
# False True
print(m(1)[0] is p)
# True
print(P.hi(p, 2)[1])
# 2
print(type(P.hi).__name__, type(p.hi).__name__)
# function method
# 실제로 다른 객체이다.

try:
    P.hi(5)
except TypeError as e:
    print("에러:", e)
# 아마 self~P자리에 5가 들어가고, x에 argument가 오지 않았으므로 찡찡댈 것...