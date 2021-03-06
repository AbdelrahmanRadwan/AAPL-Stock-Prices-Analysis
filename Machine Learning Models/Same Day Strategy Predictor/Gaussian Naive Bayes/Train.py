from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


csv_file_i = "../../../DataSet/Dataset.csv"
df = pd.read_csv(csv_file_i)


#The labels (targets)...
labels = np.array(df['same_day_strategy'])

#Adding new feature to the data frame
df["privious_day_same_day_delta"] = 1
for i in range(1, len(df)):
    temp = df["same_day_delta"][i - 1]
    df.loc[i, "privious_day_same_day_delta"] = temp

#The features (Input)...

features = df.filter(items=['Open', 'Close', "High", "Low", "Adj Close", "Volume", "privious_day_same_day_delta"])

features = np.array(features)



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

# Save the classifier
with open(r'Gaussian_Naive_Bayes_Model_Weights.pkl', 'wb') as file:
    pickle.dump(model, file)

