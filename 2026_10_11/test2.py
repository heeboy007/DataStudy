
x = 'global'

def read_only():
    print(x)

def read_then_assign():
    print(x)
    x = 'local'

read_only()
# global
try:
    read_then_assign()
except UnboundLocalError as e:
    print("에러: ", e)

count = 0

def inc():
    global count
    count += 1

inc(); inc()
print(count)
# 2

lst = []
def push():
    lst.append(1)

push(); push()
print(lst)
# [1, 1]
