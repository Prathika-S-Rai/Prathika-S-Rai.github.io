from sklearn.externals import joblib
model = joblib.load('irispred.sav')

model.predict([[5.8,2.8,5.1,2.4]])