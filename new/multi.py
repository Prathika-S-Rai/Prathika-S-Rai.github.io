import numpy as np

a = ['Delhi','Bangalore','Chennai','Mumbai']

from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()

lEncoder.fit(a)
b = lEncoder.transform(a)
c=['Chennai']
#lEncoder.fit(c)
lEncoder.transform(c)
lEncoder.inverse_transform([1])
