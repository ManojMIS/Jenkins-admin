import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df=pd.read_excel('Petal_dataset.xlsx')

X=df[['PetalLength','Petalwidth']]
y=df['Species']

encoder=LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train,X_test,y_train,y_test = train_test_split(X,y_encoded,test_size=0.3,random_state=42)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy_score=accuracy_score(y_test,y_pred)
print('Accuracy :',accuracy_score)

plt.figure(figsize=(12,0))
plot_tree(model,
          feature_names=['PetalLength','PetalWidth'],
          class_names=encoder.classes_,
          filled=True)

plt.show()