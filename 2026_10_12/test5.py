
class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        n = self.n
        while n > 0:
            yield n
            n -= 1

c = Countdown(3)

print(list(c), list(c))
# [3, 2, 1] [3, 2, 1]
it = iter(c)
print(list(it), list(it))
# [3, 2, 1] []
print(iter(c) is c, iter(it) is it)
# False True

