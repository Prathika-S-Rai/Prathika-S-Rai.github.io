import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
data=pd.read_csv('headbrain.csv')
data.head()  #toextract
x_train=np.array(data.iloc[:100,2].values)
y_train=np.array(data.iloc[:100,3].values)
x_test=np.array(data.iloc[100:,2].values)
y_test=np.array(data.iloc[100:,3].values)

#training
xm , ym = x_train.mean(),y_train.mean()
b1_num = 0.0
b1_demon = 0.0
for i in range(len(x_train)):
    b1_num += (x_train[i]-xm)*(y_train[i]-ym)
    b1_demon +=  (x_train[i]-xm)**2
b1=b1_num/b1_demon
b0 = ym-b1*xm

#y=mxtc   //test results exam pred
y_pred = b1*x_test + b0

#result
plt.scatter(x_train,y_train, color='red', label='Training')  #scattered points plot-means line
plt.scatter(x_test,y_pred, color='blue', label='Prediction')
plt.scatter(x_test,y_test, color='green', label='Actual score')
plt.legend()
plt.show()

sst = 0.0
ssr = 0.0
for i in range(len(y_test)):
    sst += (y_test[i] - y_test.mean())**2
    ssr += (y_test[i] - y_pred[i])**2
R=1-float(ssr)/float(sst)
print('score',R)
