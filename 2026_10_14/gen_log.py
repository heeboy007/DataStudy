
import random
from datetime import datetime, timedelta

random.seed(42)

USERS = ["alice", "bob", "carol", "dave", "erin"]
ACTIONS = ["login", "search", "view", "buy", "logout"]
LEVELS = ["INFO"] * 8 + ["WARN"] * 2 + ["ERROR"]
EXTRA = {"buy": 200, "search": 50}     # 이 action들은 일부러 더 느리게

N = 200_000
t = datetime(2026, 10, 1)
n_format = n_ms = 0

with open("access.log", "w", encoding="utf-8") as f:
    for i in range(N):
        t += timedelta(seconds=random.randint(0, 3))
        stamp = f"{t:%Y-%m-%d %H:%M:%S}"
        if i % 1000 == 999:
            f.write("this line is garbage\n")
            n_format += 1
        elif i % 1000 == 500:
            f.write(f"{stamp} INFO user=bob action=view ms=abc\n")
        else:
            user = random.choice(USERS)
            action = random.choice(ACTIONS)
            level = random.choice(LEVELS)
            ms = int(random.expovariate(1 / 120)) + 5 + EXTRA.get(action, 0)
            f.write(f"{stamp} {level} user={user} action={action} ms={ms}\n")

print(f"총 {N}줄 / 정상 {N - n_format - n_ms} / 형식 오류 {n_format} / ms오류 {n_ms}")