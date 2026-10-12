from dataclasses import dataclass, field, asdict, replace

@dataclass
class P:
    x: int
    y: int = 0

p, q = P(1), P(1, 0)
print(p, p == q, p is q)
# P(1, 0) True False
print(P.__hash__)
# None
# 애초에 frozen하지 않다.
print(P("a", [1]))

@dataclass(frozen=True)
class F:
    x: int
    y: int = 0

f = F(1, 2)
try:
    f.x = 5
except Exception as e:
    print(type(e).__name__)
    # FrozenInstanceError

print(len({F(1, 2), F(1, 2)}))
# 1
print(replace(f, x=9), asdict(f))
# F(9, 2), { 'x': 1, 'y': 2 }

try:
    @dataclass
    class Bad:
        items: list = []
except ValueError as e:
    print("에러:", e)

@dataclass
class Good:
    items: list = field(default_factory=list)

g1, g2 = Good(), Good()
g1.items.append(1)
print(g2.items)
# []

@dataclass(order=True)
class Ver:
    major: int
    minor: int

print(Ver(1, 2) < Ver(1, 10), sorted([Ver(2, 0), Ver(1, 5)]))
# True, [Ver(1, 5), Ver(2, 0)]