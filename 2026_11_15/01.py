
from scipy import stats
import pandas as pd
import math

#1
df = pd.read_csv("weight.csv")
mu_0 = 500

res = stats.ttest_1samp(df["weight"], popmean=mu_0)
print(round(res.statistic, 3))
print(round(res.pvalue, 4))
print(f"pvalue({res.pvalue}) is lesser than 0.05, means null hypo is rejected.")
print("... means sample weights are different(or, lesser) than expected")

#기각
#-4.391
#0.0001

#2
df = pd.read_csv("diet.csv")

res = stats.ttest_rel(df["after"], df["before"], alternative="less")
print(round(res.statistic, 2))
print(round(res.pvalue, 4))
print(f"pvalue({res.pvalue}) is lesser than 0.05, means null hypo is rejected.")
print("... means diet did proved its effectiveness")

#3
df = pd.read_csv("class_scores.csv")
df_a, df_b = df[df["group"] == "A"]["score"], df[df["group"] == "B"]["score"]

res_1 = stats.levene(df_a, df_b)
is_equal_var = res_1.pvalue >= 0.05
print(f"has equal var? : {is_equal_var}")

res_2 = stats.ttest_ind(df_a, df_b, equal_var=is_equal_var)
print(round(res_2.statistic, 2))
print(f"pvalue({res_2.pvalue}) is lesser than 0.05, means null hypo is rejected.")
print("... means gruop A and group B do not have equal means")

#4
df_c = df[df["group"] == "C"]["score"]

res = stats.f_oneway(df_a, df_b, df_c)
print(round(res.statistic, 2))
print(round(res.pvalue, 4))
print(f"pvalue({res.pvalue}) is lesser than 0.05, means null hypo is rejected.")
print("... means at least one of the group's mean is different than others")

#5
print(math.floor(df_b.mean()))

res = stats.shapiro(df_a)
print(round(res.pvalue, 3))
print(f"pvalue({res.pvalue}) is not lesser than 0.05, means null hypo is not rejected.")
print("... means it is ok to assume normalness of the distribution")
