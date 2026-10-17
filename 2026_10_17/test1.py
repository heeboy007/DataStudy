import pandas as pd

with open("access.log", encoding="utf-8") as f:
    raw = pd.Series(f.read().splitlines(), name="raw")

pattern = r"^(?P<ts>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) action=(?P<action>\w+) ms=(?P<ms>\S+)$"
df = raw.str.extract(pat=pattern)
df["ms"] = pd.to_numeric(df["ms"], errors="coerce")

fmt_err = df["user"].isna()
ms_err = df["user"].notna() & df["ms"].isna()
clean = df[~fmt_err & ~ms_err].astype({"ms": "int32"})

print(len(df), fmt_err.sum(), ms_err.sum(), len(clean))
print(clean.dtypes)

print(clean.memory_usage(deep=True))
print(clean.memory_usage(deep=True).sum() / 1e6, "MB")

cat = clean.astype({ "level": "category", "user": "category", "action": "category" })
print(cat.memory_usage(deep=True).sum() / 1e6, "MB")
print(cat["level"].cat.categories, cat["level"].cat.codes.dtypes)