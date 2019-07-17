import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('insurance.csv')

data.columns
x = np.array(data.iloc[:,0:6].values)
y = np.array(data.iloc[:,6].values)

from sklearn.preprocessing import LabelEncoder

l1Encoder = LabelEncoder()
l4Encoder = LabelEncoder()
l5Encoder = LabelEncoder()

x[:,1] = l1Encoder.fit_transform(x[:,1])
x[:,4] = l4Encoder.fit_transform(x[:,4])
x[:,5] = l5Encoder.fit_transform(x[:,5])

from sklearn.preprocessing import OneHotEncoder
ohEncoder = OneHotEncoder(categorical_features=[5])
x = ohEncoder.fit_transform(x).toarray()
x = x[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)
#score = regressor.score(x_test,y_test)

x_in = input("Enter the input(,) ")
x_i = x_in.split(',')
# 45,male,23,2,no,southeast
#for i in range(len(x_i)):
a = []
for i in x_i:
    try:
        a.append(float(i))
    except:
       # a.lowercase(i)
        a.append(i.lower())

a = np.array(a).reshape(1,-1)
a[:,1] = l1Encoder.transform(a[:,1])
a[:,4] = l4Encoder.transform(a[:,4])
a[:,5] = l5Encoder.transform(a[:,5])

a = ohEncoder.transform(a).toarray()
a = a[:,1:]
regressor.predict(a)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,y_pred)**(1/2) 

