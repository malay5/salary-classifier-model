from flask import Flask,render_template,request,url_for
import pickle
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return f"My name is {name}"

@app.route("/users_get",methods=["GET"])
def users_get():
    return { "id": 1,"name": "John Doe", "email": "john12@gmail.com"}

@app.route("/result",methods=["POST"])
def success():
    user={}
    age=request.form['age']
    li=['age', 'workclass', 'education', 'marital-status', 'occupation',
       'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
       'hours-per-week', 'native-country']
    query=[]
    for i in li:
        exec(f"query.append(int(request.form['{i}']))")
    with open('pickle_model','rb') as f:
        model=pickle.load(f)
    result= model.predict([query])[0]
    print(query)
    print(model)
    print(result)
    if result==0:
        return "The ideal income for the selected person would be <= $50K"
    elif result==1:
        return "The ideal income for the selected person would be >$50K"
    else:
        return "Something is wrong"

with app.test_request_context():
    url_for('Home')
    url_for('user',name='Malay')