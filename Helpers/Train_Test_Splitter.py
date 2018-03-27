import math
def split_train_test(df):
    #using 70% of the data as training
    train_size = math.floor(70/100 * len(df))
    #use the rest of the data as testing (30%)
    test_size = len(df) - train_size

    '''
    The data layouts
    '''
    label_names = [0, 1]
    feature_names = ["same_day_delta"]

    '''
    Data of the Training
    - the labels
    - the features
    '''
    #The labels (targets)...
    training_labels = list(df['same_day_strategy'][:train_size])
    #The features (Input)...
    training_features = list(df['same_day_delta'][:train_size])

    '''
    Data of the Testing
    - the labels
    - the features
    '''
    #The labels (targets)...
    testing_labels = list(df['same_day_strategy'][train_size:])
    #The features (Input)...
    testing_features = list(df['same_day_delta'][train_size:])
