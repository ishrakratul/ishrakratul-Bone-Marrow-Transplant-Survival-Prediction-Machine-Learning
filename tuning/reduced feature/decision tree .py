import warnings
import time
to=time.clock()
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler 
scale=StandardScaler()
x="../input/xtrain/x_train_11.csv"
y="../input/ytrain/y_train_11.csv"
x=pd.read_csv (x)
x=x.drop('Unnamed: 0',axis=1)
x=scale.fit_transform(x)
y=pd.read_csv (y)
y=y.drop('Unnamed: 0',axis=1)
grid={
    'criterion' : ['gini', 'entropy'],
    'splitter':['best', 'random'],
    'min_samples_split': [1,2,3,4,5],
    'min_samples_leaf':[1,3,5,6,7,8,9],
    'max_depth':[3,5,7,'NONE']
}
model=DecisionTreeClassifier()
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("DecisionTree accuracy:",rdm.best_score_)
print("DecisionTree accuracy:",rdm.best_params_)
t1=time.clock()
print(t1-to)
