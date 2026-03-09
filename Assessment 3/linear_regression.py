import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data=pd.read_excel("housing_prices.xlsx")

print(data)

X=data[['Size (sq ft)','Bedrooms']]

y=data['Price']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
print("Mean sqayre Error ",mse)

print('\n Model co efficient :')
print("Size co efficient :",model.coef_[0])
print("Bedrooms coefficient :",model.coef_[1])
print("Intercept:",model.intercept_)


plt.scatter(y_test,y_pred)
plt.xlabel=("Actual price")
plt.ylabel=("Predicted price")
plt.title("Actual vs Predicted Housing prices")

plt.show()