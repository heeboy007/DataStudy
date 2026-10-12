
class Dog:
    kind = 'canine'
    tricks = []

    def __init__(self, name):
        self.name = name

    def add(self, trick):
        self.tricks.append(trick)

a, b = Dog('a'), Dog('b')
a.add('sit')
print(b.tricks)
# ['sit']

a.kind = 'wolf'
print(a.kind, b.kind, Dog.kind)
# 'wolf' 'canine' 'canine'
print(a.__dict__, b.__dict__)
# { 'kind': 'wolf' } {}
# {'name': 'a', 'kind': 'wolf'} {'name': 'b'}
del a.kind
print(a.kind)
# 'canine'

a.tricks = ['x']
print(a.tricks, b.tricks, Dog.tricks)
# ['x'] ['sit'] ['sit']