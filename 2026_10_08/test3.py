
d = {'b': 1, 'a': 2}
d['c'] = 3
del d['b']
d['b'] = 4
print(list(d))
# ['a', 'c', 'b']

try:
    for k in d:
        if d[k] > 2:
            del d[k]
except RuntimeError as e:
    print("에러:", e)

for k in list(d):
    if d[k] > 2:
        del d[k]
print(d)
# {'a': 2}

from collections import defaultdict, Counter
words = "a b a c b a".split()

c1 = {}
for w in words:
    if w in c1:
        c1[w] += 1
    else:
        c1[w] = 1

c2 = {}
for w in words:
    c2[w] = c2.get(w, 0) + 1

c3 = defaultdict(int)
for w in words:
    c3[w] += 1

c4 = Counter(words)
print(c1 == c2 == dict(c3) == dict(c4)) 
# True
print(c4.most_common(2))
# [('a', 3), ('b', 2)] 
# 제일 흔한거 2개
