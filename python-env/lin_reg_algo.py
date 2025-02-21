import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def LIN_REG_ALGO(df, quote):
    forecast_out = int(7)
    
    # Filter data for the specific company (quote)
    company_data = df[df['Code'] == quote].copy()
    
    # Create the 'Close after n days' column by shifting 'Close' values
    company_data['Close after n days'] = company_data['Close'].shift(-forecast_out)
    
    # Prepare the data
    df_new = company_data[['Close', 'Close after n days']]

    # Handle missing values by imputing them with the mean
    imputer = SimpleImputer(strategy='mean')
    df_new = pd.DataFrame(imputer.fit_transform(df_new), columns=df_new.columns)

    # Define the target variable and the feature matrix
    y = np.array(df_new.iloc[:-forecast_out, -1])
    y = np.reshape(y, (-1, 1))  # Ensure correct shape for fitting
    
    X = np.array(df_new.iloc[:-forecast_out, 0:-1])
    X_to_be_forecasted = np.array(df_new.iloc[-forecast_out:, 0:-1])

    # Split the data into training and test sets (80% train, 20% test)
    X_train = X[0:int(0.8 * len(df_new)), :]
    X_test = X[int(0.8 * len(df_new)):, :]
    y_train = y[0:int(0.8 * len(df_new)), :]
    y_test = y[int(0.8 * len(df_new)):, :]

    # Standardize the data
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    X_to_be_forecasted = sc.transform(X_to_be_forecasted)

    # Train a Linear Regression model
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)

    # Predict on the test set
    y_test_pred = clf.predict(X_test)
    y_test_pred = y_test_pred * 1.04  # Adjust the prediction

    # Compute the RMSE (Root Mean Squared Error)
    error_lr = np.sqrt(mean_squared_error(y_test, y_test_pred))

    # Forecast for the next 'forecast_out' days
    forecast_set = clf.predict(X_to_be_forecasted)
    forecast_set = forecast_set * 1.04  # Adjust the forecast

    # Get the predicted value for the next time step
    lr_pred = forecast_set[0, 0]

    lr_pred = float(lr_pred)
    error_lr = float(error_lr)

    # Return the data, predicted value, forecasted values, and RMSE error
    return company_data, lr_pred, forecast_set, error_lr
