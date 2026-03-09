import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df=pd.read_excel("Spending_score.xlsx")

print(df.head())

X=df.select_dtypes(include=['float64','int64'])

scaler=StandardScaler()
X_Scaled=scaler.fit_transform(X)

k=3
kmeans=KMeans(n_clusters=k,random_state=42)

cluster=kmeans.fit_predict(X_Scaled)

df['Clusters']=cluster

print(df)

plt.scatter(X_Scaled[:,0],
            X_Scaled[:,1],c=cluster)
plt.xlabel("Income")
plt.ylabel("Age")
plt.title("K-Means clustering")
plt.show()