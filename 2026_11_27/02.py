import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
print(train.shape, test.shape)
print(train.dtypes)

# 1
print(train.isna().sum())

# fill na with median, usually because they tend to be robust to outliers
train["monthly"] = train["monthly"].fillna(train["monthly"].median())
# fill with mode, not many options here for non-numneric types...
train["contract"] = train["contract"].fillna(train["contract"].mode()[0])

# 2
y_col = "churn"
y = train[y_col]
X = train.drop(columns=["id", y_col], errors="ignore")
X_test = test.drop(columns=["id"], errors="ignore")

#get to one-hot encoding
both = pd.concat([X, X_test], keys=["train", "test"])
both = pd.get_dummies(both)
X, X_test = both.loc["train"], both.loc["test"]

X_tr, X_va, y_tr, y_va = train_test_split(X, y, test_size=0.2, random_state=42)

#so you fit first
model = RandomForestClassifier(
    # n_estimators=300,
    # max_depth=5,
    random_state=42).fit(X_tr, y_tr)

print("val auc:", roc_auc_score(y_va, model.predict_proba(X_va)[:, 1]))

#and fit again
model.fit(X, y)
pred = model.predict_proba(X_test)[:, 1]     # 확률 vs 클래스는 지문 확인: predict()

out = pd.DataFrame({"churn_prob": pred})            # 지시된 컬럼명, 열 1개
out.to_csv("result.csv", index=False)         # 지시된 파일명, 경로 없이

chk = pd.read_csv("result.csv")
print(chk.shape, chk.columns.tolist(), chk.head(3))
print(len(chk) == len(test))