class Bag:
    def __init__(self, *items):
        self._items = list(items)
    def __len__(self):
        return len(self._items)
    def __getitem__(self, key):
        return self._items[key]
    def __contains__(self, x):
        print("  __contains__ 호출")
        return x in self._items

b = Bag(10, 20, 30)
print(len(b), b[0], b[-1], b[0:2])
# 3, 10, 30, [10, 20]

print(20 in b)
#   __contains__ 호출
# True

print(list(b))
# [10, 20, 30]

print(sorted(b, reverse=True), max(b), sum(b))
# [30, 20, 10] 30 60

print(bool(Bag()), bool(b))
# False True

