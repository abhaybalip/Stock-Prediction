from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
from arima_algo import ARIMA_ALGO
from lstm_algo import LSTM_ALGO
from lin_reg_algo import LIN_REG_ALGO
import pandas as pd

app = Flask(__name__)
CORS(app)
# Function to download historical stock data
def get_historical(quote):
    try:
        data = yf.download(quote, period="2y", interval="1d")
        if data.empty:
            raise ValueError(f"No data found for stock symbol: {quote}")
        data.to_csv(f'{quote}.csv')
        return data
    except Exception as e:
        raise ValueError(f"Error downloading data: {str(e)}")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve JSON data from the POST request
        content = request.get_json()

        # Validate that 'nm' is in the request JSON
        if 'nm' not in content:
            return jsonify({'error': 'Missing stock symbol (nm) in request'}), 400
        
        quote = content['nm']
        
        # Get historical data for the stock symbol
        df = get_historical(quote)
        
        # Perform predictions using the different algorithms
        arima_pred, error_arima = ARIMA_ALGO(df, quote)
        lstm_pred, error_lstm = LSTM_ALGO(df,quote)
        df, lr_pred, forecast_set, error_lr = LIN_REG_ALGO(df,quote)
        
        # Return the predictions in JSON format
        return jsonify({
            'stock': quote,
            'algo_output': [
                {'algorithm': 'ARIMA', 'prediction': arima_pred, 'error': error_arima},
                {'algorithm': 'LSTM', 'prediction': lstm_pred, 'error': error_lstm},
                {'algorithm': 'Linear Regression', 'prediction': lr_pred, 'error': error_lr}
            ]
        })

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
