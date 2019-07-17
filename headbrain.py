import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#data=pd.read_csv('headbrain.csv')
#data.head()  #toextract
#a=data["Head Size(cm^3)"].values
#


data1=pd.read_csv('Salary_Data.csv')
data1.head()  #toextract
a1=data1["Salary"].values
a2=data1.iloc[:,0:1].values
a3=data1.iloc[:,1].values

#plt.scatter(a2,a3,color='Blue')  #display the graph

from sklearn.model_selection import train_test_split

a2_train,a2_test,a3_train,a3_test=train_test_split(a2,a3,test_size=2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(a2_train,a3_train)
m=regressor.coef_
c=regressor.intercept_

y75=m*7.5+c
yp75=regressor.predict([[7.5]])

#plt.scatter(a2_train,a3_train,color="red")
#plt.plot(a2_train,regressor.predict(a2_train),color="Blue")


a3_pred=regressor.predict(a2_test)

plt.scatter(a2_train,a3_train,color="red")
plt.plot(a2_test,regressor.predict(a2_test),color="Yellow")
plt.plot(a2_test,a3_test,color="Green")
plt.plot(a2_train,regressor.predict(a2_train),color="Blue")
