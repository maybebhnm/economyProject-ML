# xGboost model:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_absolute_error


housesDB = pd.read_csv('./housePrice.csv')

X = housesDB[['Area', 'Room', 'Parking', 'Warehouse', 'Elevator']]
Y = housesDB['Price(USD)']

data_dmatrix = xgb.DMatrix(data=X,label=Y)

for i in [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]:
    # devide database to train and test:
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=i, random_state=1) 

    xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)

    xg_reg.fit(X_train,Y_train)

    Y_pred = xg_reg.predict(X_test)

    RMSE = np.sqrt(mean_squared_error(Y_test, Y_pred))
    Rsquare = r2_score(Y_test, Y_pred)
    MAPE = mean_absolute_percentage_error(Y_test, Y_pred)
    MAE = mean_absolute_error(Y_test, Y_pred)

    print('R-square: ' + str(Rsquare) +'\tRMSE: '+ str(RMSE)+'\tMAPE: '+ str(MAPE)+'\tMAE: '+ str(MAE))

