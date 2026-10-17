
from analyze import analyze
import pandas as pd

with open("access.log", encoding="utf-8") as f:
    raw = pd.Series(f.read().splitlines(), name="raw")

pattern = r"^(?P<ts>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) action=(?P<action>\w+) ms=(?P<ms>\S+)$"
df = raw.str.extract(pat=pattern)
df["ms"] = pd.to_numeric(df["ms"], errors="coerce")

fmt_err = df["user"].isna()
ms_err = df["user"].notna() & df["ms"].isna()
clean = df[~fmt_err & ~ms_err].astype({"ms": "int32"})

by_level = clean["level"].value_counts()
pair_count = clean.groupby(["user", "action"]).size()
avg_ms = clean.groupby("action")["ms"].mean()

res = analyze("access.log")

print(dict(res["by_level"]) == by_level.to_dict())
print(res["pair_count"] == pair_count.to_dict())
print(all(abs(res["avg_ms"][a] - v) < 1e-9 for a, v in avg_ms.items()))
print(type(pair_count.index))
