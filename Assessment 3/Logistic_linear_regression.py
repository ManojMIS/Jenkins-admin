import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_report


data=pd.read_excel("spam_data.xlsx")

print(data)

X=data[['Email Length','Has Link']]

y=data['is Spam']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)


acc=accuracy_score(y_test,y_pred)
prec=precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)

print(acc)

print(prec)

print(rec)

print(classification_report(y_test,y_pred))
plt.scatter(y_test,y_pred)
plt.xlabel=("Actual pred")
plt.ylabel=("Predicted prd")
plt.title("Actual vs Predicted values")
plt.show()