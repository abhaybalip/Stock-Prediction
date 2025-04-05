import math
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.callbacks import EarlyStopping
from Graph import generate_graph

def LSTM_ALGO(df, quote):
    df = df[df['Code'] == quote].copy()

    train_size = int(0.8 * len(df))
    dataset_train = df[:train_size]
    dataset_test = df[train_size:]

    training_set = dataset_train[['Close']].values
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)

    X_train, y_train = [], []
    for i in range(7, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-7:i, 0])
        y_train.append(training_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(50))
    model.add(Dropout(0.2))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

    dataset_total = pd.concat([dataset_train['Close'], dataset_test['Close']], axis=0)
    inputs = dataset_total[len(dataset_total) - len(dataset_test) - 7:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)

    X_test = []
    for i in range(7, len(inputs)):
        X_test.append(inputs[i-7:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    predicted_price = model.predict(X_test)
    predicted_price = sc.inverse_transform(predicted_price)
    real_price = dataset_test[['Close']].values

    error_lstm = math.sqrt(mean_squared_error(real_price, predicted_price))

    last_sequence = X_train[-1]
    X_forecast = np.reshape(last_sequence, (1, last_sequence.shape[0], 1))
    forecast_price = model.predict(X_forecast)
    forecast_price = sc.inverse_transform(forecast_price)

    lstm_pred = float(forecast_price[0, 0])
    error_lstm = float(error_lstm)

    generate_graph(real_price, predicted_price, 'LSTM', quote)
    return lstm_pred, error_lstm
