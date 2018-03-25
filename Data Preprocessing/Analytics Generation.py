''''
Uses the data generated from the Preprocessing phase to make some analytics
and save them to the DataSet folder in 
'''
from dateutil import parser
import pandas as pd
import math
import datetime


#paths of the dataset and the meta data...
csv_file_i = "../DataSet/Dataset.csv"

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
for date in df["Date"]:
    _Date = datetime.datetime.strptime(date, "%Y-%m-%d")
    data["Year"].append(_Date.year)
    data["Month"].append(_Date.month)

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
        constructiv_data[_Date.year][_Date.month]["MaxClosePrice"] = 0

    if "MinOpenPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinOpenPrice"] = 0

    if "MaxHighPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MaxHighPrice"] = 0

    if "MaxLowPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MaxLowPrice"] = 0

    if "MinHighPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinHighPrice"] = 0

    if "MinLowPrice" not in constructiv_data[_Date.year][_Date.month]:
        constructiv_data[_Date.year][_Date.month]["MinLowPrice"] = 0

    #Update all the values in the dictionary with the current record
