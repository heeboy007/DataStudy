# gen_type3.py
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)

# 세 반 점수 (독립 두 집단 + 세 집단 비교용)
n = 40
pd.DataFrame({
    "group": np.repeat(["A", "B", "C"], n),
    "score": np.concatenate([
        rng.normal(70, 10, n), rng.normal(76, 10, n), rng.normal(70.5, 10, n)
    ]).round(1),
}).to_csv("class_scores.csv", index=False)

# 다이어트 전후 체중 (대응표본용)
m = 30
before = rng.normal(72, 8, m)
after = before - rng.normal(2.5, 3, m)
pd.DataFrame({"id": range(1, m + 1),
              "before": before.round(1), "after": after.round(1)}
             ).to_csv("diet.csv", index=False)

# 제품 무게 (단일표본용)
pd.DataFrame({"weight": rng.normal(497.5, 6, 50).round(1)}
             ).to_csv("weight.csv", index=False)

# 심어 둔 정답(모집단 값)은 파일로만 저장. 문제를 다 푼 뒤에 열어 보세요
with open("truth.txt", "w", encoding="utf-8") as f:
    f.write("class_scores: 모평균 A=70, B=76, C=70.5, 표준편차 10 (반별 40명)\n")
    f.write("diet: 평균 감소량 2.5kg (표준편차 3, 30명)\n")
    f.write("weight: 모평균 497.5g, 표준편차 6 (50개)\n")