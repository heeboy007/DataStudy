
def count_up(n):
    print("시작")
    for i in range(n):
        print(f" yield bef {i}")
        yield i
        print(f" yield aft {i}")
    print("끝")

gen = count_up(2)

print("생성 완료")
print(next(gen))
print(next(gen))

try:
    next(gen)
except StopIteration:
    print("StopIteration")

# 생성 완료
# 시작
#  yield bef 0
# 0
#  yield aft 0
#  yield bef 1
# 1
#  yield aft 1
# 끝
# StopIteration