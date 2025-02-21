import os
import math
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd
from datetime import datetime

def ARIMA_ALGO(df, quote):
    # Filter the dataframe for the specified company symbol (quote)
    df['Code'] = quote  # Add the stock symbol as a column
    company_data = df[df["Code"] == quote]

    # Ensure that 'Date' is a column and not the index
    if 'Date' not in company_data.columns:
        company_data.reset_index(inplace=True)
    
    # Set 'Date' column as datetime index
    def parser(x):
        return datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S')

    # Extract the 'Price' column and 'Date' column
    company_data['Price'] = company_data['Close']
    quantity_date = company_data[['Price', 'Date']]

    # Convert 'Date' to datetime
    quantity_date.index = quantity_date['Date'].map(lambda x: parser(x))
    
    # Ensure 'Price' is of type float
    quantity_date['Price'] = quantity_date['Price'].map(lambda x: float(x))
    
    # Handle missing data by backfilling
    quantity_date = quantity_date.fillna(quantity_date.bfill())
    quantity_date = quantity_date.drop(['Date'], axis=1)

    # Convert to a numpy array for ARIMA
    quantity = quantity_date.values
    size = int(len(quantity) * 0.80)  # Use 80% for training, 20% for testing
    train, test = quantity[0:size], quantity[size:]

    # Function for ARIMA model prediction
    def arima_model(train, test):
        history = [x for x in train]
        predictions = list()
        for t in range(len(test)):
            model = ARIMA(history, order=(6, 1, 0))  # ARIMA parameters (p,d,q)
            model_fit = model.fit()
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            obs = test[t]
            history.append(obs)
        return predictions

    # Get predictions using ARIMA
    predictions = arima_model(train, test)
    
    # Last prediction and RMSE (Root Mean Square Error)
    arima_pred = predictions[-1]  # Last predicted value
    error_arima = math.sqrt(mean_squared_error(test, predictions))  # RMSE for evaluation

    arima_pred = float(arima_pred)
    error_arima = float(error_arima)
    return arima_pred, error_arima
