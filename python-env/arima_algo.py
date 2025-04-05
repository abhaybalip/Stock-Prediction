import math
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd
from datetime import datetime
from Graph import generate_graph

def ARIMA_ALGO(df, quote):
    df = df[df["Code"] == quote].copy()

    if 'Date' not in df.columns:
        df.reset_index(inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Price'] = df['Close'].astype(float)
    df = df[['Price']].fillna(method='bfill')

    data = df.values
    size = int(len(data) * 0.8)
    train, test = data[:size], data[size:]

    def arima_model(train, test):
        history = [x for x in train]
        predictions = []
        for t in range(len(test)):
            model = ARIMA(history, order=(6, 1, 0))
            model_fit = model.fit()
            output = model_fit.forecast()
            predictions.append(output[0])
            history.append(test[t])
        return predictions

    predictions = arima_model(train, test)
    arima_pred = float(predictions[-1])
    error_arima = math.sqrt(mean_squared_error(test, predictions))

    generate_graph(test, predictions, 'ARIMA', quote)
    return arima_pred, error_arima
