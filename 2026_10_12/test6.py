
class Money:
    def __init__(self, v):
        self.v = v
    def __repr__(self):
        return f"Money({self.v})"
    def __add__(self, o):
        if isinstance(o, Money):
            return Money(self.v + o.v)
        return NotImplemented
    def __radd__(self, o):
        if o == 0:
            return self
        return NotImplemented
    def __lt__(self, other):
        return self.v < other.v

print(Money(1) + Money(2))
# Money(3)

try:
    Money(1) + 5
except TypeError as e:
    print("에러:", e)

print(sum([Money(1), Money(2), Money(3)]))
# Money(6)
print(sorted([Money(3), Money(1)]))
# [Money(1), Money(3)]
print(Money(1) > Money(3))
# False