import warnings
warnings.filterwarnings("ignore")
import time
to=time.clock()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
import xgboost as xgb
from sklearn.preprocessing import StandardScaler 
scale=StandardScaler()
x="../input/xtrain-all/x_train_all.csv"
y="../input/ytrain-all/y_train_all.csv"
x=pd.read_csv (x)
x=x.drop('Unnamed: 0',axis=1)
x=scale.fit_transform(x)
y=pd.read_csv (y)
y=y.drop('Unnamed: 0',axis=1)
grid={'max_depth': [3,6, 18, 1],
        'gamma': [0,1,9],
        'colsample_bytree' : [0.5,1],
        'min_child_weight' : [0, 10, 1],
      'n_estimators':[2,10,100],
      'learning_rate':[0.1,0.5,1]
}
model=xgb.XGBClassifier(eval_metric='error')
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("XGB accuracy:",rdm.best_score_)
print("XGB accuracy:",rdm.best_params_)
t1=time.clock()
print(t1-to)
