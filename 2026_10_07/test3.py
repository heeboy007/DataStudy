
def f(n, lst):
    n += 1
    lst.append(99)

num = 5
data = [1, 2]
f(num, data)
print(num, data)
# 5 [1, 2, 99]

def g(lst):
    lst = [0, 0, 0]

g(data)
print(data)
# [1, 2, 99]

# 2/2 correct