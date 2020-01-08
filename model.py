from flask import Flask, jsonify
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import xml.etree.cElementTree as et
import requests
import time
from tqdm import tqdm
import ipywidgets as widgets
from IPython.display import display
from fastkml import kml
import math
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from flask import render_template
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, GridSearchCV
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.pipeline import Pipeline

app = Flask(__name__)

#import data
newtrain = pd.DataFrame('../data/newtrain.csv')

# selecting features

features = ['bathrooms', 'bedrooms', 'flatkind', 'floor_area_sqm',
            'rafflestime', 'remaining_lease','BEDOK', 'BISHAN', 'BUKIT BATOK',
            'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA',
            'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST',
            'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS',
            'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON',
            'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN', 'year', 'closest_pschool',
            '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']

#split train dataset
X_train, X_val, y_train, y_val = train_test_split(newtrain[features],\
                                                  newtrain['resale_price'],\
                                                  test_size = 0.3,\
                                                  random_state = 42)

#normalising data
ss = StandardScaler()
ss.fit(X_train)
X_train_ss = ss.transform(X_train)
X_val_ss = ss.transform(X_val)

#model
rfr = RandomForestRegressor()
modelrfr = rfr.fit(X_train_ss, y_train)


pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))


    # predrfr = rfr.predict(X_val_ss)
    # testpredrfr = rfr.predict(X_test_ss)

    # logreg = LogisticRegression()
    # model = logreg.fit(df[['Speed']].values, df["student"].values)

    # @app.route('/json-test')
    # def json_test():
    #     return jsonify(my_data)

    # @app.route('/predict-price')
    # def predict_student():
    #     speed = request.args.get("speed")
    #     if speed:
    #         predicted = model.predict([[float(speed)]]).tolist()
    #         probabilities = model.predict_proba([[float(speed)]]).tolist()
    #         result = {
    #             "response": "ok", 
    #             "predictions": predicted,   
    #             "probabilities": {student: probabilities[0][index] for index, student in enumerate(model.classes_.tolist())}
    #         } 
    #     else:
    #         result = {"response": "not found", "message": "Please provide a model parameter to predict!"}
    #     return jsonify(result)

    # @app.route('/predict-flower', methods = ["GET", "POST"])
    # def predict_flower():

    #     output = None

    #     if request.method == "POST":
    #         sepal_len = float(request.form["sepal_length"])
    #         sepal_width = float(request.form["sepal_width"])
    #         petal_len = float(request.form["petal_length"])
    #         petal_width = float(request.form["petal_width"])
    #         prediction = model.predict([[float(sepal_len), float(sepal_width), float(petal_len), float(petal_width)]])
    #         prob = model.predict_proba([[float(sepal_len), float(sepal_width), float(petal_len), float(petal_width)]])
            

        return render_template("base.html", output = output)
