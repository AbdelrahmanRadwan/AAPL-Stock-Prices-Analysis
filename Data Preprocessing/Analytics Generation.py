''''
Uses the data generated from the Preprocessing phase to make some analytics
and save them to the DataSet folder in 
'''
from dateutil import parser
import pandas as pd
import sys
import math
import datetime

#Maximim float value in python
MAX = sys.float_info.max
#paths of the dataset and the meta data...
csv_file_i = "../DataSet/Dataset.csv"
csv_file_o = "../DataSet/monthly_analysis.csv"
#load the input in a data frame
df = pd.read_csv(csv_file_i)

#the dictionary that we will convert into csv later (works as the data in the dataframe)
data = dict()

#Create slots for each thing needed in the analytics
data["Year"] = list()
data["Month"] = list()
data["Average_Close_Price"] = list()
data["Average_Open_Price"] = list()
data["Highest_Close_Price"] = list()
data["Lowest_Open_Price"] = list()
data["Highest_High_Price"] = list()
data["Highest_Low_Price"] = list()
data["Lowest_High_Price"] = list()
data["Lowest_Low_Price"] = list()

#Extract the first day from the dataset
First_Date = datetime.datetime.strptime(df["Date"][0], "%Y-%m-%d")
#Add the first year and month appeared in the dataset
data["Year"].append(First_Date.year)
data["Month"].append(First_Date.month)
#Add all the years and their months in the data
for i in range(1,len(df)):
    CurrentDate = datetime.datetime.strptime(df["Date"][i], "%Y-%m-%d")
    LastDate = datetime.datetime.strptime(df["Date"][i-1], "%Y-%m-%d")

    if CurrentDate.year != LastDate.year or CurrentDate.month != LastDate.month:
        data["Year"].append(CurrentDate.year)
        data["Month"].append(CurrentDate.month)

# A dictionary to build the analytics in - it works as a O(1) holder (for attacks) for the analytics
constructiv_data = dict()

#Build the base for the analytics in the constructiv_data dictionary
'''''
The base data are (for each month in the year):
- SumClosePrice
- SumOpenPrice
- CountOfDays
- MaxClosePrice
- MinOpenPrice
- MaxHighPrice
- MaxLowPrice
- MinHighPrice
- MinLowPrice
'''''
for i in range(len(df)):
    _Date = datetime.datetime.strptime(df["Date"][i], "%Y-%m-%d")
    #Check if the needed keys are not included in the dictionary - add it
    if _Date.year not in constructiv_data:
        constructiv_data[_Date.year] = dict()

    if _Date.month not in constructiv_data[_Date.year]:
        constructiv_data[_Date.year][_Date.month] = dict()

    #Check for the first value added - intialize with zero so we can increment later
    if "SumClosePrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["SumClosePrice"] = 0

    if "SumOpenPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["SumOpenPrice"] = 0

    if "CountOfDays" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["CountOfDays"] = 0

    if "MaxClosePrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MaxClosePrice"] = -MAX

    if "MinOpenPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinOpenPrice"] = MAX

    if "MaxHighPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MaxHighPrice"] = -MAX

    if "MaxLowPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MaxLowPrice"] = -MAX

    if "MinHighPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinHighPrice"] = MAX

    if "MinLowPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinLowPrice"] = MAX

    #Update all the values in the dictionary with the current record
    constructiv_data[_Date.year][_Date.month]["SumClosePrice"]+=df["Close"][i]
    constructiv_data[_Date.year][_Date.month]["SumOpenPrice"]+=df["Open"][i]
    constructiv_data[_Date.year][_Date.month]["CountOfDays"]+=1
    constructiv_data[_Date.year][_Date.month]["MaxClosePrice"] = max(constructiv_data[_Date.year][_Date.month]["MaxClosePrice"], df["Close"][i])
    constructiv_data[_Date.year][_Date.month]["MinOpenPrice"] = min(constructiv_data[_Date.year][_Date.month]["MinOpenPrice"], df["Open"][i])
    constructiv_data[_Date.year][_Date.month]["MaxHighPrice"] = max(constructiv_data[_Date.year][_Date.month]["MaxHighPrice"], df["High"][i])
    constructiv_data[_Date.year][_Date.month]["MaxLowPrice"] = max(constructiv_data[_Date.year][_Date.month]["MaxLowPrice"], df["Low"][i])
    constructiv_data[_Date.year][_Date.month]["MinHighPrice"] = min(constructiv_data[_Date.year][_Date.month]["MinHighPrice"], df["High"][i])
    constructiv_data[_Date.year][_Date.month]["MinLowPrice"] = min(constructiv_data[_Date.year][_Date.month]["MinLowPrice"], df["Low"][i])

# Construct the analytics csv file
for i in range(len(data["Year"])):
    year = data["Year"][i]
    month = data["Month"][i]
    data["Average_Close_Price"].append(constructiv_data[year][month]["SumClosePrice"]/constructiv_data[year][month]["CountOfDays"])
    data["Average_Open_Price"].append(constructiv_data[year][month]["SumOpenPrice"]/constructiv_data[year][month]["CountOfDays"])
    data["Highest_Close_Price"].append(constructiv_data[year][month]["MaxClosePrice"])
    data["Lowest_Open_Price"].append(constructiv_data[year][month]["MinOpenPrice"])
    data["Highest_High_Price"].append(constructiv_data[year][month]["MaxHighPrice"] )
    data["Highest_Low_Price"].append(constructiv_data[year][month]["MaxLowPrice"])
    data["Lowest_High_Price"].append(constructiv_data[year][month]["MinHighPrice"])
    data["Lowest_Low_Price"].append(constructiv_data[year][month]["MinLowPrice"])

analytics_df = pd.DataFrame(data=data)
analytics_df.to_csv(csv_file_o, index=False)
