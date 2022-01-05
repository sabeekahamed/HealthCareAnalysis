import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import tree
pf=pd.read_csv('Result.csv')
pf=pf[pf.cured==1]
kf=pf
labels = np.array(pf['regimen'])
pf=pf.drop('regimen',axis=1)
pf=pf.drop('id',axis=1)
pf=pf.drop('cured',axis=1)
pf_list=list(pf.columns)
ttf=np.array(pf)
from sklearn.model_selection import train_test_split
train_df, test_df, train_labels, test_labels = train_test_split(ttf, labels, test_size = 0.25, random_state = 42)
predict=tree.DecisionTreeClassifier()
predict.fit(train_df,train_labels)
pred=predict.predict([[0,1,1,0,1,0]])
print(pred)
