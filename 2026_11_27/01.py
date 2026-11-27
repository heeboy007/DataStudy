
import pandas as pd
import math

df_e = pd.read_csv("employees.csv")

#1
df_e_na_cols = df_e.apply(lambda col: col.isna().astype(int).sum(), axis=0)
print(df_e_na_cols)
#결과로는 salary가 제일 결측값이 많고, 25행이 결측

#2
df_e_dedup = df_e.drop_duplicates()
print(df_e_dedup.shape)
# 300행

#3
df_e_dedup = df_e.drop_duplicates()
df_e_salary_na = df_e["salary"].isna()
median_salary = df_e["salary"].median()

df_e_salary_patched = df_e["salary"].where(~df_e_salary_na, median_salary)
print(round(df_e_salary_patched.mean(), 2))
# 4728.9

#4
q3_salary = df_e_salary_patched.quantile(0.75)
q1_salary = df_e_salary_patched.quantile(0.25)
print(q3_salary, q1_salary)

iqr_salary = q3_salary - q1_salary
outliers = (df_e_salary_patched > q3_salary + iqr_salary * 1.5) | \
    (df_e_salary_patched < q1_salary - iqr_salary * 1.5)
print(outliers.astype(int).sum())
# 7 of them

#5
df_d = pd.read_csv("dept.csv")

df_m = pd.merge(df_e, df_d, how="left")
dept_name_na_count = df_m["dept_name"].isna().astype(int).sum()
sanity_check = df_m.shape[0] == df_e.shape[0]

print(f"dept_name_na_count : {dept_name_na_count}, sanity_check {sanity_check}")

def get_na_to_median_mean(cols):
    cols_na_map = cols.isna()
    return round(cols.where(~cols_na_map, cols.median()).mean(), 1)

df_m_nmm = {g:get_na_to_median_mean(df_g["salary"]) for (g, df_g) in df_m.groupby("dept_id")}
print(df_m_nmm)
# "영업": 4910.9, "인사": 4919.6 가 제일크다!

#6
print(df_m["city"].value_counts(dropna=True))
print(df_m["city"].value_counts(dropna=False))
# 서울, 부산, 대구가 제일 많고, dropna가 꺼져있으면 추가적으로 NaN = 15, 결측값 15인거 알수 있음.

#7
df_e_dedup = df_e.drop_duplicates()
df_e_dedup_dropna = df_e_dedup[~df_e_dedup["age"].isna()]
df_e_drop_na_mean_age = math.floor(df_e_dedup_dropna["age"].mean())
df_e_sorted = df_e_dedup_dropna.sort_values(by="age", ascending=False)
df_e_top5_salary_mean = df_e_sorted[0:5]["salary"].mean()

print(f"df_e_drop_na_mean_age: {df_e_drop_na_mean_age}, df_e_top5_salary_mean: {df_e_top5_salary_mean}")

#8
df_e_jd_asdate = pd.to_datetime(df_e_dedup["join_date"])
df_e_jd_asyear = df_e_jd_asdate.dt.year
print(df_e_jd_asyear.value_counts())
#tie to 2019, 2018, 38 people.