import pandas as pd
import numpy as np
from scipy import stats

#1
f_obs = np.array([90, 55, 35, 20])
f_exp = np.array([80, 60, 40, 20])

res = stats.chisquare(f_obs=f_obs, f_exp=f_exp)
print(f"chisquare_pvalue : {res.pvalue}")
#결론은 일단 기각 못했으니, 그 비율이 맞다고 가정해도 좋다.

#2
df = pd.read_csv("survey.csv")
ct = pd.crosstab(df["channel"], df["bought"])

res = stats.chi2_contingency(ct)
print(round(res.statistic, 2))
print(round(res.pvalue, 4))
print(res.dof)
print(round(res.expected_freq.min(), 2))
print(round(res.expected_freq.min(), 2) > 5)

#3
ct = np.array([[30, 20], [18, 32]])
res = stats.chi2_contingency(ct, correction=True)
print(round(res.statistic, 2))

res = stats.chi2_contingency(ct, correction=False)
print(round(res.statistic, 2))
#correction이 해석하면 보정 아닙니까? 문제는 이딴식으로 안꼽니다.

#4
group_a = np.array([12, 15, 11, 14, 13, 17])
group_b = np.array([10, 12, 9, 11])

var_a, var_b, df_a, df_b = group_a.var(ddof=1), group_b.var(ddof=1), len(group_a) - 1, len(group_b) - 1
print(var_a, var_b, df_a, df_b)

if df_a >= df_b:
    F, d1, d2 = var_a / var_b, df_a, df_b
else:
    F, d1, d2 = var_b / var_a, df_b, df_a

p_two = min(1.0, 2 * min(stats.f.cdf(F, d1, d2), stats.f.sf(F, d1, d2)))
print(round(F, 2), round(p_two, 4))

#합동 분산 추정량
pooled_var = (df_a * var_a + df_b * var_b) / (df_a + df_b)
print(round(pooled_var, 3))

se = np.sqrt(pooled_var * (1 / len(group_a) + 1 / len(group_b)))
t_stat_manual = (group_a.mean() - group_b.mean()) / se
p_val_manual = 2 * stats.t.sf(abs(t_stat_manual), df=df_a + df_b)
print(t_stat_manual, p_val_manual)

res = stats.ttest_ind(group_a, group_b, equal_var=True)
print(res)

#print(stats.chisquare.__doc__[:1500])  

#5
a = stats.poisson.pmf(2, mu=4)          # 정확히 2건
b = stats.poisson.cdf(2, mu=4)          # 2건 이하
c = stats.poisson.sf(4, mu=4)           # 5건 이상 (= 4 초과)
d = stats.binom.pmf(2, n=20, p=0.1)
e = stats.binom.cdf(2, n=20, p=0.1)
f = stats.binom.sf(2, n=20, p=0.1)      # 3건 이상 (= 2 초과)
print(a, b, c, d, e, f)