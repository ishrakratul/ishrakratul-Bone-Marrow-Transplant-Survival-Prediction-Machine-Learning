import warnings
warnings.filterwarnings("ignore")
import time
to=time.clock()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler 
scale=StandardScaler()
x="../input/xtrain-all/x_train_all.csv"
y="../input/ytrain-all/y_train_all.csv"
x=pd.read_csv (x)
x=x.drop('Unnamed: 0',axis=1)
x=scale.fit_transform(x)
y=pd.read_csv (y)
y=y.drop('Unnamed: 0',axis=1)
grid={'max_depth': [1,3,5,7,9],
      'n_estimators':[2,10,50,100],
      'learning_rate':[0.001,0.01,0.1,0.5,1],
}
model=GradientBoostingClassifier()
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("GRB accuracy:",rdm.best_score_)
print("GRB accuracy:",rdm.best_params_)
t1=time.clock()
print(t1-to)
