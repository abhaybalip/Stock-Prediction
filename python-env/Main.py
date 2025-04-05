import base64
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

from arima_algo import ARIMA_ALGO
from lstm_algo import LSTM_ALGO
from lin_reg_algo import LIN_REG_ALGO
from get_history import get_historical
from Graph import generate_graph

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

def encode_image_from_file(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        content = request.get_json()
        symbol = content.get('nm', '').upper().strip()
        if not symbol:
            return jsonify({'error': 'Missing or invalid stock symbol (nm)'}), 400

        logging.info(f"Fetching data for: {symbol}")
        df = get_historical(symbol)

        arima_pred, error_arima = ARIMA_ALGO(df, symbol)
        lstm_pred, error_lstm = LSTM_ALGO(df, symbol)
        df, lr_pred, _, error_lr = LIN_REG_ALGO(df, symbol)

        image_paths = {
            'ARIMA': f'./graph/{symbol}_ARIMA.png',
            'LSTM': f'./graph/{symbol}_LSTM.png',
            'Linear Regression': f'./graph/{symbol}_Linear_Regression.png'
        }

        base64_graphs = {
            algo: encode_image_from_file(path)
            for algo, path in image_paths.items()
        }

        predictions = sorted([
            {'algorithm': 'ARIMA', 'prediction': arima_pred, 'error': error_arima, 'graph': base64_graphs['ARIMA']},
            {'algorithm': 'LSTM', 'prediction': lstm_pred, 'error': error_lstm, 'graph': base64_graphs['LSTM']},
            {'algorithm': 'Linear Regression', 'prediction': lr_pred, 'error': error_lr, 'graph': base64_graphs['Linear Regression']}
        ], key=lambda x: x['error'])

        return jsonify({
            'stock': symbol,
            'algo_output': predictions
        })

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logging.exception("Unhandled error occurred")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
