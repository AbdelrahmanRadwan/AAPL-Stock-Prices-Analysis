from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

csv_file_i = "../../DataSet/Dataset.csv"
df = pd.read_csv(csv_file_i)


label_names = [0, 1]
feature_names = ["same_day_delta"]
#The labels (targets)...
labels = list(df['same_day_strategy'])
#The features (Input)...
features = list(df['same_day_delta'])



# Split our data to be 33% testing - the rest for training
train, test, train_labels, test_labels = train_test_split(features,
                                                        labels,
                                                        test_size=0.33,
                                                        random_state=42)
# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model = gnb.fit(train, train_labels)


