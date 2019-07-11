import numpy as np
import pandas as pd

data = pd.read_csv('50_Startups.csv')

data.columns
x = data.iloc[:,:4].values
y = data.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder

lEncoder = LabelEncoder()
x[:,3] = lEncoder.fit_transform(x[:,3])  #extracts the value and then fit it into the given variable

#assigning dummi values is called one hot encoder
from sklearn.preprocessing import OneHotEncoder

ohEncoder = OneHotEncoder(categorical_features=[3])
 
x=ohEncoder.fit_transform(x).toarray()
#x = x[:,1:]  #without first column
