words = ['banana', 'Apple', 'cherry', 'apple', 'Banana']
print(sorted(words))
# ['Apple', 'Banana', 'apple', 'banana', 'cherry']

print(sorted(words, key=str.lower))
# ['Apple', 'apple', 'banana', 'Banana', 'cherry']

r = words.sort()
print(r, words)
# None, ['banana', 'Apple', 'cherry', 'apple', 'Banana']

pairs = [('a', 2), ('b', 1), ('c', 2), ('d', 1)]
print(sorted(pairs, key=lambda p: p[1]))
# [('b', 1), ('d', 1), ('a', 2), ('c', 2)]
print(sorted(pairs, key=lambda p: -p[1]))
# [('a', 2), ('c', 2), ('b', 1), ('d', 1)]