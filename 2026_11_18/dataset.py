from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
df = df.drop(columns="target")
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df.to_csv("iris.csv", index=False)
print(df.shape, df["species"].value_counts().to_dict())