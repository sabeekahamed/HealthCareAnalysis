import pandas as pd
import numpy as np
df=pd.read_csv('First.csv')
labels = np.array(df['tb'])
print(labels)
df=df.drop('tb',axis=1)
df_list=list(df.columns)
df_list
tf=np.array(df)
# Using Skicit-learn to split data into training and testing sets
from scikit_learn.model_selection import train_test_split
# Split the data into training and testing sets
train_df, test_df, train_labels, test_labels = train_test_split(tf, labels, test_size = 0.25, random_state = 42)
print('Training Features Shape:', train_df.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_df.shape)
print('Testing Labels Shape:', test_labels.shape)
# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_df, train_labels);
# Use the forest's predict method on the test data
predictions = rf.predict(test_df)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)

print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2))
# Import tools needed for visualization

