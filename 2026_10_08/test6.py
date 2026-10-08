
nums = [2, 4, 6, 1]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
# [4, 1]

import time, random
N = 200_000
data = list((range(N)))
s = set(data)
queries = [random.randrange(N * 2) for _ in range(2000)]

t = time.perf_counter()
sum(q in data for q in queries)
t_list = time.perf_counter() - t

t = time.perf_counter()
sum(q in s for q in queries)
t_set = time.perf_counter() - t

print(f"list: {t_list:.4f}s  set: {t_set:.6f}s  배율: {t_list / t_set:.0f}x")
# 평균 O(3/4N) * 2000 vs O(1) * 2000  
# 15만배...?
