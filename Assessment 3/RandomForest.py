import pandas  as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df=pd.read_excel('EnergyConsumption_data.xlsx')
df['Date']=pd.to_datetime(df['Date'])

df['Date']=df['Date'].map(pd.Timestamp.toordinal)


X=df[['Date','Temperature','Humidity']]
y=df['EnergyConsumption']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

model = RandomForestRegressor(n_estimators=100,
                              random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

r2=r2_score(y_test,y_pred)
print('R2 score :',r2)

print("Actual :",list(y_test))

print("Predicted :",list(y_pred))