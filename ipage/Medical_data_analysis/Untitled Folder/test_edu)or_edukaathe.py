import pandas as pd
import numpy as np
df=pd.read_csv('First.csv')
labels = np.array(df['tb'])
tk=df.tb.values
df=df.drop('tb',axis=1)
df_list=list(df.columns)
df=df.drop('id',axis=1)
df_list1=list(df.columns)
tf=np.array(df)
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_df, test_df, train_labels, test_labels = train_test_split(tf, labels, test_size = 0.25, random_state = 42)
# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_df, train_labels);
predictions = rf.predict([[0,0,0,1,0,0]])      #inputs
if(predictions):
    print("you need to take test:")
else:
    print("You doesnt affected by tb")
