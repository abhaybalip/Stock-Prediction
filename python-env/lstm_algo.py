import math
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.callbacks import EarlyStopping

def LSTM_ALGO(df, quote):
    # Filter data for the specific company (quote)
    company_data = df[df['Code'] == quote].copy()
    
    # Split the data into training and testing sets (80% train, 20% test)
    dataset_train = company_data.iloc[0:int(0.8 * len(company_data)), :]
    dataset_test = company_data.iloc[int(0.8 * len(company_data)):, :]
    
    # Extract the 'Close' prices for training and testing
    training_set = dataset_train.iloc[:, 4:5].values
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    
    # Prepare training data (X_train, y_train)
    X_train = []
    y_train = []
    for i in range(7, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-7:i, 0])
        y_train.append(training_set_scaled[i, 0])
    
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    # Build the LSTM model
    regressor = Sequential()
    regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    regressor.add(Dropout(0.1))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.1))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.1))
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.1))
    regressor.add(Dense(units=1))
    
    regressor.compile(optimizer='adam', loss='mean_squared_error')
    
    # Use early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='loss', patience=10, restore_best_weights=True)
    regressor.fit(X_train, y_train, epochs=50, batch_size=32, callbacks=[early_stopping])
    
    # Prepare the testing set
    real_stock_price = dataset_test.iloc[:, 4:5].values
    dataset_total = pd.concat((dataset_train['Close'], dataset_test['Close']), axis=0)
    testing_set = dataset_total[len(dataset_total) - len(dataset_test) - 7:].values
    testing_set = testing_set.reshape(-1, 1)
    testing_set = sc.transform(testing_set)
    
    # Prepare X_test
    X_test = []
    for i in range(7, len(testing_set)):
        X_test.append(testing_set[i-7:i, 0])
    
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    # Predict the stock prices using the LSTM model
    predicted_stock_price = regressor.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    
    # Calculate the error (RMSE)
    error_lstm = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))
    
    # Forecast the next stock price
    X_forecast = np.array(X_train[-1, 1:])
    X_forecast = np.append(X_forecast, y_train[-1])
    X_forecast = np.reshape(X_forecast, (1, X_forecast.shape[0], 1))
    
    forecasted_stock_price = regressor.predict(X_forecast)
    forecasted_stock_price = sc.inverse_transform(forecasted_stock_price)
    
    # The predicted stock price for the next time step
    lstm_pred = forecasted_stock_price[0, 0]
    
    # Convert lstm_pred and error_lstm to native Python float using tolist() to convert numpy arrays to lists
    lstm_pred = float(lstm_pred)
    error_lstm = float(error_lstm)
    
    # Return the prediction and the error
    return lstm_pred,error_lstm




