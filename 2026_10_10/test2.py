words = ['apple', 'Banana', 'cherry', 'avocado']
by_first = {w[0].lower(): w for w in words}
print(by_first)
# { 'b': 'Banana', 'c': 'cherry', 'a':'avocado' }
# {'a': 'avocado', 'b': 'Banana', 'c': 'cherry'}
# 순서가 다름
print({ len(w) for w in words })
# { 5, 6, 7 }
print({ v: k for k, v in by_first.items() })
# { 'Banana': 'b', 'cherry': 'c', 'avocado': 'a' }