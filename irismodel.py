from flask import Flask,request,render_template#to create web server
import numpy as np
from sklearn.externals import joblib
app=Flask(__name__,static_folder='public')

@app.route('/')
def index():
    return render_template('irisfl.html')
@app.route('/display',methods=['POST'])
def display():
    model=joblib.load('irisPred.sav')
    slen=eval(request.form.get('sepal length'))
    swid=eval(request.form.get('sepal width')) 
    plen=eval(request.form.get('petal length')) 
    pwid=eval(request.form.get('petal width')) 
    pred=model.predict([[slen,swid,plen,pwid]])
    flowers={0:"setosa",1:"versicolor",2:"virginica"}
    return """<html><body>
                    The class is: {}""".format(flowers[pred[0]])+"""
                    <br><img src='public/"""+flowers[pred[0]].lower()+""".jpeg' />
                    </body></html>"""



if __name__=='__main__':
    app.run(debug=True)