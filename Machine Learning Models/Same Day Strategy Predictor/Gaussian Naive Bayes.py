from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


csv_file_i = "../../DataSet/Dataset.csv"
df = pd.read_csv(csv_file_i)

label_names = [0, 1]
feature_names = ["same_day_delta"]
#The labels (targets)...
labels = np.array(df['same_day_strategy'])
#The features (Input)...
features = np.array(df['same_day_delta'])
# Re-shape the features vector so we can do multiplications
features = features.reshape((len(features),1))


# Split our data to be 33% testing - the rest for training
train, test, train_labels, test_labels = train_test_split(features,
                                                        labels,
                                                        test_size=0.33,
                                                        random_state=42)
# Building the Model
# Initialize our classifier
gnb = GaussianNB()
# Train our classifier
model = gnb.fit(train, train_labels)

# Evaluating the Model
preds = gnb.predict(test)

print(accuracy_score(test_labels, preds))
