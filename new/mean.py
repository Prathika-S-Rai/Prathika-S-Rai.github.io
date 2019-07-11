import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
data=pd.read_csv('headbrain.csv')
data.head()  #toextract
x=data.iloc[:,2].values   
y=data.iloc[:,3].values
xm=x.mean()
ym=y.mean()
mt=0
my=0
for i in range(len(x)):
    mt+=(x[i]-xm)*(y[i]-ym)
    my+=(x[i]-xm)**2
ft=mt/my
b0=ym-ft*xm


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
x = x.reshape(-1,1)
regressor.fit(x,y)
coef = regressor.coef_
interc = regressor.intercept_

