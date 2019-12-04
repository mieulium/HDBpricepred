#import modules
import pandas as pd 
import numpy as np 
import requests
import time

#read file
price = pd.read_csv('../data/2012price.csv')

def get_longlat_info(df, col, name_string): 
    """
    Adds longitude and latitude data to the dataframe and delays the call
    parameters
    ---------- 
    df: dataframe
    col: dataframe column
    name_string: name of output csv file (in string)
    
    Output
    ------
    name: list of new column
    df[name]: new column generated
    """

    # counter to check the number of results queried
    count = 0

    # dictionary to put the results into 
    results = {}

    # url for query API was split into 2 as query needs to be inserted in the middle of the url
    addurl1 = "https://developers.onemap.sg/commonapi/search?searchVal="
    addurl2 = "&returnGeom=Y&getAddrDetails=Y&pageNum=1"

    # start time was defined so that the scraper can check how much sleep time is needed
    start_time = time.time()

    # the column in the dataframe was iterated to query each address in the dataframe
    for a in df[col]:
        url = (addurl1+a+addurl2)
        res = requests.get(url)
        try:
            root = res.json()
            lat = root['results'][0]['LATITUDE']
            long = root['results'][0]['LONGITUDE']
            results[a] = {'full_add': a, 'lat': lat, 'long': long, 'latlong': str(lat)+','+str(long)}
            count += 1
        except:
            print(root)
            results[a] = {'full_add': a}
            count += 1
        
        # counter displayed just to show progress
        print(count)
        
        # how much time has elapsed since the start of the scraper
        elapsed_time = time.time() - start_time
        
        # sleep time calculator (SLA API query is limited to 250 calls a minute)
        if count % 250 == 0:
            print(elapsed_time)
            if elapsed_time < ((count//250)*60):
                time.sleep((((count//250)*60)-elapsed_time))
    
    # exporting the results into a csv file
    new_df = pd.DataFrame(results)
    path = "../data/"+name_string+".csv"
    new_df.to_csv(path)

# function call
get_longlat_info(price, 'full_add', '2012pricelatlong')