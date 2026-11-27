# gen_exam.py
import numpy as np
import pandas as pd

rng = np.random.default_rng(1128)

# ---------- 유형1: 직원 / 부서 ----------
n = 300
emp = pd.DataFrame({
    "emp_id": np.arange(1, n + 1),
    "dept_id": rng.integers(1, 6, n),                      # 1~5 (5번 부서는 dept.csv에 없음)
    "age": rng.integers(24, 60, n).astype(float),
    "salary": rng.normal(4500, 800, n).round(0),
    "city": rng.choice(["서울", "부산", "대구", "인천"], n, p=[0.5, 0.2, 0.15, 0.15]),
    "join_date": pd.to_datetime("2015-01-01")
                 + pd.to_timedelta(rng.integers(0, 3650, n), unit="D"),
})
emp["join_date"] = emp["join_date"].dt.strftime("%Y-%m-%d")
emp.loc[rng.choice(n, 20, replace=False), "age"] = np.nan
emp.loc[rng.choice(n, 25, replace=False), "salary"] = np.nan
emp.loc[rng.choice(n, 15, replace=False), "city"] = np.nan
emp.loc[[10, 50, 90], "salary"] = [15000, 16000, 14500]     # 이상치
emp = pd.concat([emp, emp.sample(5, random_state=1)])       # 중복 행 5개
emp.to_csv("employees.csv", index=False)

pd.DataFrame({
    "dept_id": [1, 2, 3, 4, 6],
    "dept_name": ["영업", "개발", "인사", "재무", "법무"],
}).to_csv("dept.csv", index=False)

# ---------- 유형2: 이탈 예측 ----------
m = 1000
cust = pd.DataFrame({
    "id": np.arange(1, m + 1),
    "tenure": rng.integers(1, 73, m),
    "monthly": rng.normal(65, 20, m).round(1),
    "contract": rng.choice(["month", "year", "two_year"], m, p=[0.55, 0.25, 0.20]),
    "gender": rng.choice(["M", "F"], m),
    "calls": rng.poisson(1.5, m),
})
z = (-0.5 - 0.04 * cust["tenure"] + 0.02 * (cust["monthly"] - 65)
     + 0.4 * cust["calls"]
     + np.where(cust["contract"] == "month", 0.8,
                np.where(cust["contract"] == "year", -0.2, -0.8)))
cust["churn"] = (rng.random(m) < 1 / (1 + np.exp(-z))).astype(int)
cust.loc[rng.choice(m, 60, replace=False), "monthly"] = np.nan
cust.loc[rng.choice(m, 40, replace=False), "contract"] = np.nan

train = cust.iloc[:800].copy()
test = cust.iloc[800:].copy()
test[["id", "churn"]].to_csv("test_answer.csv", index=False)   # 채점용. 풀 때는 열지 마세요
test.drop(columns="churn").to_csv("test.csv", index=False)
train.to_csv("train.csv", index=False)

# ---------- 유형3: 카이제곱 ----------
k = 400
ch = rng.choice(["email", "sms", "app"], k)
rate = np.where(ch == "app", 0.45, np.where(ch == "sms", 0.30, 0.28))
pd.DataFrame({
    "channel": ch,
    "bought": np.where(rng.random(k) < rate, "yes", "no"),
}).to_csv("survey.csv", index=False)

print("완료:", emp.shape, train.shape, test.shape, k)