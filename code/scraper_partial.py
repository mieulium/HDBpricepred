#import modules
import pandas as pd 
import numpy as np 
import requests
import time

#read file
price = pd.read_csv('../data/pricesonly.csv')

# file was split into 8 dataframes as the query was slow as 8 was max allowed to run (250 calls/min)
price1 = price[:7300]
price2 = price[7300:14600]
price3 = price[14600:21900]
price4 = price[21900:29200]
price5 = price[29200:36500]
price6 = price[36500:43800]
price7 = price[43800:51100]
price8 = price[51100:]

# raffles place latitude and longitude
raffles_lat = 1.2838767
raffles_long = 103.8514692
rafflesplace = str(raffles_lat)+','+ str(raffles_long)

# results dictionary
priced_1 = {}
priced_2 = {}
priced_3 = {}
priced_4 = {}
priced_5 = {}
priced_6 = {}
priced_7 = {}
priced_8 = {}

# API query token 
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM1MDQsInVzZXJfaWQiOjM1MDQsImVtYWlsIjoibWlldWxpdW1AZ21haWwuY29tIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cL29tMi5kZmUub25lbWFwLnNnXC9hcGlcL3YyXC91c2VyXC9zZXNzaW9uIiwiaWF0IjoxNTczNDM0NjU4LCJleHAiOjE1NzM4NjY2NTgsIm5iZiI6MTU3MzQzNDY1OCwianRpIjoiYWJlZGE1NmE3MDg3MmU5ZTY1MDRiODkwNWE4YjhlNTcifQ.6Jc7mz4GgRYfduZEsSb0kln-2qgCiwbfkqxOq9Pj4MA"

def get_routing_info(df, end, routetype, token, starttime, enddict): 
    """
    Adds longitude and latitude data to the dataframe and delays the call
    parameters
    ---------- 
    df: dataframe
    end: end point latitude and longitude
    routetype: accepts either (walk, drive, pt, cycle) as transport options
    token: generated token for email account
    time: time of transport in HH:MM:SS
    enddict: empty dict name
    
    Output
    ------
    name: list of new column
    df[name]: new column generated
    """

    # counter
    count = 1

    #url was stored in segments to allow accomodation of search parameters
    addurl1 = "https://developers.onemap.sg/privateapi/routingsvc/route?start="
    addurl2 = "&end="
    addurl3 = "&routeType="
    addurl4 = "&token="
    addurl5 = "&date="
    addurl6 = "&time="
    addurl7 = "&mode="
    mode = 'TRANSIT'
    addurl8 = "&maxWalkDistance="
    walk = '1500'
    addurl9 = "&numItineraries="
    numit = '3'

    # start time recorded 
    start_time = time.time()

    # df was iterated to find out necessary search parameters
    for i in range(len(df['latlong'])):
        add = df.iloc[i]['full_add']
        start = df.iloc[i]['latlong']
        date = df.iloc[i]['month']+'-01'
        url = (addurl1+start+addurl2+end+addurl3+routetype+addurl4
               +token+addurl5+date+addurl6+starttime+addurl7+mode+
               addurl8+walk+addurl9+numit)
        
        # API request get
        res = requests.get(url)
        
        # data to be only taken if status code is 200
        if res.status_code == 200:
            root = res.json()
            query = root["plan"]["itineraries"][0]["duration"]
            enddict[add] = {'rafflestime': query}
            count += 1

        # data to be skipped
        else: 
            enddict[add] = {'rafflestime': ""}
            count += 1

    # calculated elapsed time since scraper started            
    elapsed_time = time.time() - start_time

    # calculated sleep time needed given the amount of time that had passed and the results queried        
    if count % 250 == 0:
        print(elapsed_time)
        if elapsed_time < ((count//250)*60):
            time.sleep((((count//250)*60)-elapsed_time))

    # results exported into csv
    rafflesplacetime = pd.DataFrame(enddict)
    path = '../data/'+enddictstring+'.csv'
    rafflesplacetime.to_csv(path)

get_routing_info(price1, rafflesplace, 'pt', token, '07:00:00', priced_1, 'priced_1' )
get_routing_info(price2, rafflesplace, 'pt', token, '07:00:00', priced_2, 'priced_2' )
get_routing_info(price3, rafflesplace, 'pt', token, '07:00:00', priced_3, 'priced_3' )
get_routing_info(price4, rafflesplace, 'pt', token, '07:00:00', priced_4, 'priced_4' )
get_routing_info(price5, rafflesplace, 'pt', token, '07:00:00', priced_5, 'priced_5' )

