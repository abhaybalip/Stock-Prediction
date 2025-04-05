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
            return { error: error.message };
        }
    } else {
        return { error: "No stock symbol provided" };
    }
}

const Predict = () => {
    const [result, setResult] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [stockSymbol, setStockSymbol] = React.useState("");
    const inputRef = React.useRef(null);

    const handlePrediction = async () => {
        const ip = inputRef.current.value.trim().toUpperCase();
        if (ip) {
            setLoading(true);
            const res = await Predictor(ip);
            setLoading(false);

            if (res && res.stock && res.algo_output) {
                setResult(res);
                setStockSymbol(ip);
            } else {
                window.alert(res.error || 'No prediction available or invalid response.');
            }
        } else {
            window.alert('Please enter a stock symbol');
        }
    };

    const handleReset = () => {
        setResult(null);
        setStockSymbol("");
        setLoading(false);
        if (inputRef.current) inputRef.current.value = '';
    };

    return (
        <div className='app-main-prd'>
            <div className='prd'>
                <input
                    type='text'
                    className='prd-ip'
                    id='name'
                    placeholder='Enter stock symbol (e.g. AAPL)'
                    ref={inputRef}
                />
                <div className='prd-btn'>
                    <div className='btn-submit' onClick={handlePrediction}>Predict</div>
                    <div className='btn-reset' onClick={handleReset}>Reset</div>
                </div>

                {/* Loading Spinner */}
                {loading && (
                    <div className="loading-spinner">
                        <div className="spinner"></div>
                        <p>Loading predictions...</p>
                    </div>
                )}

                {/* Display result if available */}
                {!loading && result && result.algo_output && result.algo_output.length > 0 ? (
                    <div className="prd-res show">
                        <h3>Prediction for <strong>{stockSymbol}</strong>:</h3>
                        <div className="prediction-container">
                            {result.algo_output.map((algo, index) => (
                                <div key={index} className="prediction-item">
                                    <h4>{algo.algorithm}</h4>
                                    <p><strong>Prediction:</strong> {algo.prediction.toFixed(2)}</p>
                                    <p><strong>Error:</strong> {algo.error.toFixed(4)}</p>
                                    <img
                                        src={`data:image/png;base64,${algo.graph}`}
                                        alt={`${algo.algorithm} graph`}
                                        className='prediction-graph'
                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                ) : (!loading && result === null ? (
                    <div className="prd-res">
                        <p>Enter a stock symbol to get predictions.</p>
                    </div>
                ) : null)}
            </div>
        </div>
    );
};

export default Predict;
