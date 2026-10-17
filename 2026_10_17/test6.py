
import pandas as pd

with open("access.log", encoding="utf-8") as f:
    raw = pd.Series(f.read().splitlines(), name="raw")

pattern = r"^(?P<ts>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) action=(?P<action>\w+) ms=(?P<ms>\S+)$"
df = raw.str.extract(pat=pattern)
df["ms"] = pd.to_numeric(df["ms"], errors="coerce")

fmt_err = df["user"].isna()
ms_err = df["user"].notna() & df["ms"].isna()
clean = df[~fmt_err & ~ms_err].astype({"ms": "int32"})

clean = clean.assign(ts=pd.to_datetime(clean["ts"]))
ts = clean.set_index("ts")
print(ts.resample("1h").size().head())
err_rate = (ts["level"] == "ERROR").resample("1h").mean()
print(err_rate.describe())