import React from 'react';
import '../asset/style/Predict.css';



async function Predictor(nm) {
    if (nm) {
        try {
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ nm: nm })
            });
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
            return { "error": error.message };
        }
    } else {
        return { "error": "No stock symbol provided" };
    }
}

const Predict = () => {
    const [result, setResult] = React.useState(null);
    const [loading, setLoading] = React.useState(false);  // New state for loading
    const [stockSymbol, setStockSymbol] = React.useState("");

    const handlePrediction = async () => {
        const ip = document.querySelector('#name').value;
        if (ip) {
            setLoading(true); // Start loading when request is made
            const res = await Predictor(ip);
            setLoading(false); // Stop loading when result is received
            if (res && res.stock && res.algo_output) {
                setResult(res);
                setStockSymbol(ip);
            } else {
                window.alert('No prediction available or invalid response.');
            }
        } else {
            window.alert('Please enter a stock symbol');
        }
    };

    const handleReset = () => {
        setResult(null);
        setStockSymbol("");
        setLoading(false);  // Reset loading state
        document.querySelector('#name').value = '';
    };

    return (
        <div className='app-main-prd'>
            <div className='prd'>
                <input
                    type='text'
                    className='prd-ip'
                    id='name'
                    placeholder='Enter stock symbol'
                />
                <div className='prd-btn'>
                    <div className='btn-submit' onClick={handlePrediction}>Predict</div>
                    <div className='btn-reset' onClick={handleReset}>Reset</div>
                </div>

                {/* Loading Indicator */}
                {loading && (
                    <div className="loading-spinner">
                        <div className="spinner"></div>
                        <p>Loading...</p>
                    </div>
                )}

                {/* Display result if available */}
                {result && result.algo_output && result.algo_output.length > 0 ? (
                    <div className="prd-res show">
                        <h3>Prediction for {stockSymbol}:</h3>
                        <div className="prediction-container">
                            {result.algo_output.map((algo, index) => (
                                <div key={index} className="prediction-item">
                                    <h4>{algo.algorithm}</h4>
                                    <p><strong>Prediction:</strong> {algo.prediction}</p>
                                    <p><strong>Error:</strong> {algo.error}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                ) : (
                    <div className="prd-res">
                        <p>No predictions available.</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Predict;
