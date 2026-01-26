import warnings
warnings.filterwarnings("ignore")
import time
to=time.clock()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import StandardScaler 
scale=StandardScaler()
x="../input/xtrain/x_train_11.csv"
y="../input/ytrain/y_train_11.csv"
x=pd.read_csv (x)
x=x.drop('Unnamed: 0',axis=1)
x=scale.fit_transform(x)
y=pd.read_csv (y)
y=y.drop('Unnamed: 0',axis=1)
grid={'n_estimators':[2,10,50,100],
      'learning_rate':[0.00001,0.01,0.05,0.1,1],
}
model=AdaBoostClassifier()
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("ADA accuracy:",rdm.best_score_)
print("ADA accuracy:",rdm.best_params_)
t1=time.clock()
print(t1-to)
