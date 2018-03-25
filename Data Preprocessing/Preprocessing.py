from dateutil import parser
import pandas as pd
import numpy as np
import math
import csv

#paths of the dataset and the meta data...
csv_file_o = "/home/radwan/Desktop/AAPL Stock Prices Analysis/DataSet/Dataset.csv"
csv_file_i = "/home/radwan/Desktop/AAPL Stock Prices Analysis/Meta Data/AAPL.csv"

#load the input in a data frame
df = pd.read_csv(csv_file_i)

#new column - the days of the week, it includes the names of the days
day_of_week = list()

#new column - percentage of difference between the	Open and Close on the same day
same_day_delta = list()

#new column - binary values denoting if the same_day_delta is negative or positive
same_day_strategy = list()

#new column - the percentage for change between Close and last trading day Close
next_close_delta = list()
next_close_delta.append(0) #no change for the first day

#new column - binary values denoting if the same_day_delta is negative or positive
next_close_strategy = list()

#walk through all the Dates to extract the day's name
for date in df["Date"]:
    day_of_week.append(parser.parse(date).strftime("%a"))

#walk through all the days to extract the same day delta
#percentage difference = diff/avg * 100%
for i in range(len(df)):
    diff = df["Open"][i] - df["Close"][i]
    avg = (df["Open"][i] + df["Close"][i])/2
    same_day_delta.append(diff/avg *100)

#walk through all the days to extract the next close delta
#percentage	for	change = diff/|old value| * 100%
for i in range(1, len(df)):
    diff = df["Close"][i] - df["Close"][i-1]
    next_close_delta.append(diff/math.fabs(df["Close"][i-1]) *100)

#add a new column in the data frame with the day name
df["day_of_week"] = day_of_week

#add a new column in the data frame with the percentage of difference
df["same_day_delta"] = same_day_delta

#add a new column in the data frame with the percentage	for	change
df["next_close_delta"] = next_close_delta

#walk through all the same_day_delta values to check if they are positive or not
for delta in df["same_day_delta"]:
    if delta<=0.0:
        same_day_strategy.append(0)
    else:
        same_day_strategy.append(1)

#add a new column in the data frame with binary classifier of the day delta
df["same_day_strategy"] = same_day_strategy


#walk through all the next_close_delta values to check if they are positive or not
for delta in df["next_close_delta"]:
    if delta<=0.1:
        next_close_strategy.append(0)
    else:
        next_close_strategy.append(1)

#add a new column in the data frame with binary classifier of the day delta
df["next_close_strategy"] = next_close_strategy

#Write DateFrame back as csv file
df.to_csv(csv_file_o, index=False)
