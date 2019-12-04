# Capstone - HDB Price Prediction

This project is a part of the curriculum for General Assembly Data Science Immersive.

#### -- Project Status: [Completed]

## Problem/Objective
As the most Singaporeans first make their first big purchase when they buy their first HDB flat. This project aims to find out what are the predictors of resale HDB flats so that we can better prepare ourselves to buy a HDB of choice.

Likewise, we also hope to use the prediction to see if the price we are paying for a HDB is reasonable.

### Methods Used
* Data Cleaning
* Data Exploration
* Statistical Inference
* Data Scaling
* Modelling techniques
* Advanced Modelling techniques (Regularisation, Gradient Boosting, Regressors) 
* Data Visualization

### Technologies
* Python
* Pandas, jupyter, numpy, scipy
* Matplotlib, Seaborn
* Scikit Learn
* Requests
* AWS

## Project Description
- Data was obtained from data.gov.sg, SLA OneMap API, LTA DataMall

## Needs of this project

- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting

## Getting Started

1. Please clone this repository before using it. 
2. Datasets are kept in .csv files that are contained in [../code/]within this repo.   
3. Data processing/transformation scripts are being kept [../code/]


## Resulting Data Dictionary

### Modelling Dataframe
|Feature|Type|Description|
|---|---|---|
|'bathrooms'| Continuous | Number of bathrooms |
| 'bedrooms'| Continuous | Number of bedrooms |
| 'flatkind'| Ordinal | Flat kind where it ranges 1 = 1 room to 7 = Multigeneration |
|'floor_area_sqm'| Continuous| Size of flat by squared meters |
|'rafflestime'| Continuous | Length of time to reach Raffles Place MRT by public transportation in seconds |
|'remaining_lease'| Continuous | Length of time left on 99 year lease |
| 'BEDOK'| Dummy | Town variable|
| 'BISHAN'| Dummy | Town variable|
| 'BUKIT BATOK'| Dummy | Town variable|
|'BUKIT MERAH'| Dummy | Town variable|
| 'BUKIT PANJANG'| Dummy | Town variable|
|'BUKIT TIMAH'| Dummy | Town variable|
|'CENTRAL AREA'| Dummy | Town variable|
|'CHOA CHU KANG'| Dummy | Town variable|
|'CLEMENTI'| Dummy | Town variable|
|'GEYLANG'| Dummy | Town variable|
|'HOUGANG'| Dummy | Town variable|
|'JURONG EAST'| Dummy | Town variable|
|'JURONG WEST'| Dummy | Town variable|
|'KALLANG/WHAMPOA'| Dummy | Town variable|
|'MARINE PARADE'| Dummy | Town variable|
|'PASIR RIS'| Dummy | Town variable|
|'PUNGGOL'| Dummy | Town variable|
|'QUEENSTOWN'| Dummy | Town variable|
|'SEMBAWANG'| Dummy | Town variable|
|'SENGKANG'| Dummy | Town variable|
|'SERANGOON'| Dummy | Town variable|
|'TAMPINES'| Dummy | Town variable|
|'TOA PAYOH'| Dummy | Town variable|
|'WOODLANDS'| Dummy | Town variable|
|'YISHUN'| Dummy | Town variable|
|'year'| Continuous | Year transacted|
|'closest_pschool'| Distance in km to the nearest primary school |
|'02'| Dummy| Month transacted|
|'03'| Dummy| Month transacted|
|'04'| Dummy| Month transacted|
|'05'| Dummy| Month transacted|
|'06'| Dummy| Month transacted|
|'07'| Dummy| Month transacted|
|'08'| Dummy| Month transacted|
|'09'| Dummy| Month transacted|
|'10'| Dummy| Month transacted|
|'11'| Dummy| Month transacted|
|'12'| Dummy| Month transacted|


