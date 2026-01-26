import warnings
warnings.filterwarnings("ignore")
import time
to=time.clock()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
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
    'penalty':['l1','l2','elasticnet','none'],
    'C':np.logspace(-5,5,20),
    'solver':['lbfgs','newton-cg','liblinear','sag','saga'],
    'max_iter':[10,100]
}
model=LogisticRegression()
rdm = GridSearchCV(model,grid,cv=10)
rdm.fit(x,y)
print("Logreg accuracy:",rdm.best_score_)
print("Logreg best params:",rdm.best_params_)
t1=time.clock()
print(t1-to)
