from dateutil import parser
import pandas as pd
import numpy as np
import csv

#paths of the dataset and the meta data...
csv_file_o = "/home/radwan/Desktop/AAPL Stock Prices Analysis/DataSet/Dataset.csv"
csv_file_i = "/home/radwan/Desktop/AAPL Stock Prices Analysis/Meta Data/AAPL.csv"

#load the input in a data frame
df = pd.read_csv(csv_file_i)
#new column - the days of the week, it includes the names of the days
day_of_week = list()

#walk through all the Dates to extract the day's name
for date in df["Date"]:
    day_of_week.append(parser.parse(date).strftime("%a"))

#add a new column in the data frame with the day name
df["day_of_week"]=day_of_week


#Write DateFrame back as csv file
df.to_csv(csv_file_o, index=False)
