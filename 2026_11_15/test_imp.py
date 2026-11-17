
import xgboost
import lightgbm
from sklearn.datasets import load_iris

df = load_iris(as_frame=True).frame
df["species"] = df["target"].map(dict(enumerate(load_iris().target_names)))
df.drop(columns="target").to_csv("iris.csv", index=False)