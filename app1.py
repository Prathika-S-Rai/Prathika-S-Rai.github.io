from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("templates.html")

"""@app.route('/compute')
def compute():
    a=10
    b=20
    c=a+b
    return "Sum of {} and {} is {}".format(a,b,c)
    """
@app.route('/display',methods=['POST'])
def display():
    name = request.form.get('name')
    print(name)
    return 'hello '+name
#webserver is created
if __name__ == '__main__':
    app.run(debug=True)
    