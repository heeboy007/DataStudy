from scipy import stats
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

def is_null_rejected(result, alpha=0.05):
    if result.pvalue < alpha:
        return True
    return False

df = pd.read_csv("iris.csv")

#1
res = stats.pearsonr(df["sepal_length"], df["petal_length"])
print(f"stat: {round(res.statistic, 3)}, is_rejected: {is_null_rejected(res)}")

res = stats.spearmanr(df["sepal_length"], df["petal_length"])
print(f"stat: {round(res.statistic, 3)}, is_rejected: {is_null_rejected(res)}")

#2
grouped_df = {g[0]:g[1] for g in df.groupby("species")}

grouped_petal_length = [g["petal_length"] for g in grouped_df.values()]
res = stats.levene(*grouped_petal_length)
is_equal_var = not is_null_rejected(res)
print(f"is_equal_var: {is_equal_var}")

res = stats.f_oneway(*grouped_petal_length)
print(f"stat: {round(res.statistic, 2)}, is_rejected: {is_null_rejected(res)}, pvalue: {round(res.pvalue, 4)}")

#3
versicolor_pw = grouped_df["versicolor"]["petal_width"]
virginica_pw = grouped_df["virginica"]["petal_width"]

res = stats.levene(versicolor_pw, virginica_pw)
is_equal_var = not is_null_rejected(res)
print(f"is_equal_var: {is_equal_var}")

res = stats.ttest_ind(versicolor_pw, virginica_pw, equal_var=is_equal_var)
print(f"stat: {round(res.statistic, 2)}, is_rejected: {is_null_rejected(res)}")
print(f"versicolor: {versicolor_pw.mean()}, virginica: {virginica_pw.mean()}")

#4
#model fitting 1
X = sm.add_constant(df["petal_length"])
y = df["petal_width"]
simple_model_1 = sm.OLS(y, X).fit()
print(simple_model_1.summary())

#model fitting 2
simple_model_2 = smf.ols("petal_width ~ petal_length", data=df).fit()
print(simple_model_2.summary())

#same thing... 

#making third model wo bias
X = df["petal_length"]
y = df["petal_width"]
simple_model_3 = sm.OLS(y, X).fit()
print(simple_model_3.summary())

#5
X = sm.add_constant(df[["petal_length", "petal_width", "sepal_width"]])
y = df["sepal_length"]
multi_model = sm.OLS(y, X).fit()
print(multi_model.summary())
print(round(multi_model.params["petal_length"], 2))
print(round(multi_model.rsquared, 4))
#every X value is significant

#6
mask_df = (df.species == "virginica") | (df.species == "versicolor")
new_df = df[mask_df]
new_df.insert(0, "is_virginica", (new_df["species"] == "virginica").astype(int))

logit_model = smf.logit("is_virginica ~ petal_length", data=new_df).fit()
print(logit_model.summary())

conf = logit_model.conf_int()
or_table = pd.DataFrame({
    'or': round(np.exp(logit_model.params), 2),
    '2.5%': np.exp(conf[0]),
    '97.5%': np.exp(conf[1]),
    'pvalue': logit_model.pvalues
})

print(or_table)

res = stats.shapiro(df["petal_length"])