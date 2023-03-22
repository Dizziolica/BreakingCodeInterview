import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

transactions = pd.read_csv("Fraud.csv")


x = transactions.drop("isFraud", axis=1)
y = transactions["is_fraud"]

x = pd.get_dummmies(x)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)


print("Acuracia do modelo:", accuracy)
