
import pandas as pd

with open("access.log", encoding="utf-8") as f:
    raw = pd.Series(f.read().splitlines(), name="raw")

pattern = r"^(?P<ts>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) action=(?P<action>\w+) ms=(?P<ms>\S+)$"
df = raw.str.extract(pat=pattern)
df["ms"] = pd.to_numeric(df["ms"], errors="coerce")

fmt_err = df["user"].isna()
ms_err = df["user"].notna() & df["ms"].isna()
clean = df[~fmt_err & ~ms_err].astype({"ms": "int32"})
pair_count = clean.groupby(["user", "action"]).size()

g = clean.groupby("action")["ms"]
print(g.agg(["count", "mean", "median", "max"]))
print(g.quantile(0.95))

summary = clean.groupby("action").agg(
    n=("ms", "size"), mean_ms=("ms", "mean"), p95=("ms", lambda s: s.quantile(0.95))
)
print(summary)

print(pair_count.unstack())
print(pd.crosstab(clean["user"], clean["action"]))
