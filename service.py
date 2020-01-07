from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
import pandas as pd
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

my_data = [
    {"student": "Anthony", "Speed": 15.25, "Power": "over 9000"},
    {"student": "Ruairi", "Speed": 28, "Power": "over 9000"},
    {"student": "Sam", "Speed": 12.58, "Power": "over 9000"},
    {"student": "Evan", "Speed": 30.23, "Power": "over 9000"},
]
df = pd.DataFrame(my_data)

logreg = LogisticRegression()
model = logreg.fit(df[['Speed']].values, df["student"].values)

@app.route('/json-test')
def json_test():
    return jsonify(my_data)

@app.route('/predict-student')
def predict_student():
    speed = request.args.get("speed")
    if speed:
        predicted = model.predict([[float(speed)]]).tolist()
        probabilities = model.predict_proba([[float(speed)]]).tolist()
        result = {
            "response": "ok", 
            "predictions": predicted, 
            "probabilities": {student: probabilities[0][index] for index, student in enumerate(model.classes_.tolist())}
        } 
    else:
        result = {"response": "not found", "message": "Please provide a model parameter to predict!"}
    return jsonify(result)

@app.route('/predict-student-interface', methods = ["GET", "POST"])
def predict_student_interface():

    output = None

    if request.method == "POST":
        speed = float(request.form["speed"])
        output = model.predict([[speed]])[0]

    return render_template("base.html", output = output)