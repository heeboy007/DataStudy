import time
from analyze import analyze
import pandas as pd

t = time.perf_counter()
analyze("access.log")
t_py_all = (time.perf_counter() - t) * 1000

t = time.perf_counter()
with open("access.log", encoding="utf-8") as f:
    raw = pd.Series(f.read().splitlines(), name="raw")

pattern = r"^(?P<ts>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) action=(?P<action>\w+) ms=(?P<ms>\S+)$"
df = raw.str.extract(pat=pattern)
df["ms"] = pd.to_numeric(df["ms"], errors="coerce")

fmt_err = df["user"].isna()
ms_err = df["user"].notna() & df["ms"].isna()
clean = df[~fmt_err & ~ms_err].astype({"ms": "int32"})
t_pd_fetch = (time.perf_counter() - t) * 1000

t = time.perf_counter()
_ = clean.groupby(["user", "action"])["ms"].mean()
t_pd_group = (time.perf_counter() - t) * 1000

t = time.perf_counter()
cat = clean.astype({ "level": "category", "user": "category", "action": "category" })
_ = cat.groupby(["user", "action"])["ms"].mean()
t_pd_cat = (time.perf_counter() - t) * 1000

print(f"t_py_all:{t_py_all}, t_pd_fetch:{t_pd_fetch}, t_pd_group:{t_pd_group}, t_pd_cat:{t_pd_cat}")

x = clean.copy()
x.loc[x.index[:5], "user"] = None
print(x.groupby("user").size().sum(), len(x))
print(x.groupby("user", dropna=False).size().sum())