
import pandas as pd

a = pd.Series([1, 2, 3], index=["x", "y", "z"])
b = pd.Series([10, 20, 30], index=["z", "x", "w"])

print(a + b)
print(a.to_numpy() + b.to_numpy())
print(a.add(b, fill_value=0))

d = pd.DataFrame({"v": [1, 2, 3, 4]})
sub = d[d["v"] > 2]
sub["w"] = 0
d.loc[d["v"] > 2, "w"] = 0
print(d)