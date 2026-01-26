import warnings
warnings.filterwarnings("ignore")
import time
to=time.clock()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler 
scale=StandardScaler()
x="../input/xtrain-all/x_train_all.csv"
y="../input/ytrain-all/y_train_all.csv"
x=pd.read_csv (x)
x=x.drop('Unnamed: 0',axis=1)
x=scale.fit_transform(x)
y=pd.read_csv (y)
y=y.drop('Unnamed: 0',axis=1)
grid={
    'n_neighbors':[2,5,10,100],
    'weights':['uniform','distance'],
    'leaf_size':[2,5,10,30,50],
    'p':[1,2,4]
}
model=KNeighborsClassifier()
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("KNN accuracy:",rdm.best_score_)
print("KNN best params:",rdm.best_params_)
t1=time.clock()
print(t1-to)
