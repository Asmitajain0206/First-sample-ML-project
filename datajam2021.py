# -*- coding: utf-8 -*-
"""datajam2021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E0GgwVcabeUfkQligoVge2oH3Gw25ia2
"""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn import svm

all_data_path = "/content/train.csv"

all_data = pd.read_csv(all_data_path)

all_data.head()

all_data.isnull().sum()

all_data.mean()

all_data=all_data.fillna(all_data.mean())

all_data.isnull().sum()

X_train, X_val= train_test_split(all_data, test_size=0.2, random_state=42)

X_train,y_train = X_train.drop(['motor_UPDRS','Id'], axis=1),X_train.drop(['subject','Id','age','sex','test_time','total_UPDRS','Jitter(%)','Jitter(Abs)','Jitter:RAP','Jitter:PPQ5','Jitter:DDP','Shimmer','Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','NHR','HNR','RPDE','DFA','PPE'], axis=1)
X_val, y_val = X_val.drop(['motor_UPDRS','Id'], axis=1),X_val.drop(['subject','Id','age','sex','test_time','total_UPDRS','Jitter(%)','Jitter(Abs)','Jitter:RAP','Jitter:PPQ5','Jitter:DDP','Shimmer','Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','NHR','HNR','RPDE','DFA','PPE'], axis=1)

X_train

y_train

X_val

y_val

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()

regressor = svm.SVR()

X_train.isnull().sum()

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_val)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_val,y_pred)

print("MSE of the model is :" ,mse)

pred_csv_path = "/content/test.csv"

pred_csv = pd.read_csv(pred_csv_path)

final_test_path = "/content/test.csv"
final_test = pd.read_csv(final_test_path)

final_test.head()

final_test = final_test.drop(['Id'],axis=1)

predictions = regressor.predict(final_test)

submission = {
    'Id': pred_csv.Id.values, 
    'motor_UPDRS': predictions 
}

solution = pd.DataFrame(submission)
solution.head()

solution.to_csv('submission.csv',index=False)

