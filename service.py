import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict',methods=['POST'])
def predict():
    town = request.form.get("town", None)
    flatkind = request.form.get("flatkind", None)
    floor_area_sqm = int(request.form.get("floor_area_sqm", None))
    remaining_lease = int(request.form.get("remaining_lease", None))
    address = request.form.get("address", None)
    bathroom = int(request.form.get("bathroom", None))
    bedroom = int(request.form.get("bedroom", None))
    month = int(request.form.get("month", None))

    # url for query API was split into 2 as query needs to be inserted in the middle of the url
    addurl1 = "https://developers.onemap.sg/commonapi/search?searchVal="
    addurl2 = "&returnGeom=Y&getAddrDetails=Y&pageNum=1"

    url = (addurl1+address+addurl2)
    res = requests.get(url)

    root = res.json()
    lat = root['results'][0]['LATITUDE']
    long = root['results'][0]['LONGITUDE']
    results = str(lat)+','+str(long)

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM1MDQsInVzZXJfaWQiOjM1MDQsImVtYWlsIjoibWlldWxpdW1AZ21haWwuY29tIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cL29tMi5kZmUub25lbWFwLnNnXC9hcGlcL3YyXC91c2VyXC9zZXNzaW9uIiwiaWF0IjoxNTc4NDQ4NTE0LCJleHAiOjE1Nzg4ODA1MTQsIm5iZiI6MTU3ODQ0ODUxNCwianRpIjoiMDVkY2M4OTFhNDk5OGMyMWY3MzA0MzE1ZDM1ZTIwNmIifQ.PJ_UdoBDDMy0jJjzKjuXfaq3BIoBVs0IQVGl3WW9jYo"

    url2 = "https://developers.onemap.sg/privateapi/routingsvc/route?start="+results+"&end=1.2838767,103.8514692&routeType=pt&token="+token+"&date=2020-01-08&time=07:00:00&mode=TRANSIT&maxWalkDistance=1500&numItineraries=3"
    timeres = requests.get(url2)
    if timeres.status_code == 200:
            root = timeres.json()
            query = root["plan"]["itineraries"][0]["duration"]
            rafflestime= query

    closest_pschool = 0.4
    year = 2020

    ## town
    townlist = ['BEDOK', 'BISHAN', 'BUKIT BATOK',
                'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA',
                'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST',
                'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS',
                'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON',
                'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN']
    town_bin = []
    for x in townlist:
        if town == x:
            town_bin.append(1)
        else:
            town_bin.append(0)

    ##month
    monthlist = [2,3,4,5,6,7,8,9,10,11,12]
    month_bin = []
    for m in monthlist:
        if month == m:
            month_bin.append(1)
        else:
            month_bin.append(0)

    #all var
    features = [bathrooms, bedrooms, flatkind, floor_area_sqm,
            rafflestime, remaining_lease] + town_bin +[year, closest_pschool] + month_bin

    modelfeatures = [np.array(features)]
    prediction = model.predict(modelfeatures)

    output = round(prediction[0], 2)
    return render_template("dropdown.html", prediction_text='Price should be $ {}'.format(output))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
