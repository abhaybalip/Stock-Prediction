import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from Graph import generate_graph

def LIN_REG_ALGO(df, quote):
    forecast_out = 7
    company_data = df[df['Code'] == quote].copy()
    company_data['Close after n days'] = company_data['Close'].shift(-forecast_out)

    df_new = company_data[['Close', 'Close after n days']]
    imputer = SimpleImputer(strategy='mean')
    df_new = pd.DataFrame(imputer.fit_transform(df_new), columns=df_new.columns)

    y = df_new.iloc[:-forecast_out, 1].values.reshape(-1, 1)
    X = df_new.iloc[:-forecast_out, 0].values.reshape(-1, 1)
    X_forecast = df_new.iloc[-forecast_out:, 0].values.reshape(-1, 1)

    X_train = X[:int(0.8 * len(X))]
    X_test = X[int(0.8 * len(X)):]
    y_train = y[:int(0.8 * len(y))]
    y_test = y[int(0.8 * len(y)):]

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    X_forecast = scaler.transform(X_forecast)

    model = LinearRegression(n_jobs=-1)
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test) * 1.04
    forecast_set = model.predict(X_forecast) * 1.04
    lr_pred = float(forecast_set[0, 0])
    error_lr = float(np.sqrt(mean_squared_error(y_test, y_test_pred)))

    generate_graph(y_test, y_test_pred, 'Linear_Regression', quote)
    return company_data, lr_pred, forecast_set, error_lr
