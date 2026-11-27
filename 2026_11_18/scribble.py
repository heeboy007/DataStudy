
from scipy import stats
import pandas as pd

def is_from_normal_dist(res, alpha=0.05):
    return res.pvalue >= alpha

def is_equal_var(res, alpha=0.05):
    return res.pvalue >= alpha

iris = pd.read_csv("iris.csv")

res = stats.shapiro(iris["petal_width"])
print(f"normal? : {is_from_normal_dist(res)}")

res = stats.bartlett(iris["petal_width"], iris["petal_length"])
print(f"equal var? : {is_equal_var(res)}")

