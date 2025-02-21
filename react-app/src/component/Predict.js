
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
            })
            const data = await response.json()
            return data
        } catch (error) {
            console.error('Error:', error)
            return { "error": error.message }
        }
    } else {
        return { "error": "No name provided" }
    }
}


const Predict = () => {
    const [result, setResult] = React.useState(null);

    return (
        <div className='app-main-prd'>
            <div>
                <input type='text' id='name' placeholder='Enter stock symbol' />

                <div onClick={async () => {
                    const ip = document.querySelector('#name').value
                    if (ip) {
                        const res = await Predictor(ip)
                        setResult(res)
                    } else {
                        window.alert('Please enter a stock symbol');
                    }
                }}>Predict</div>

                <div onClick={() => {
                    setResult(null); // Reset the result
                    document.querySelector('#name').value = ''; // Clear input field
                }}>Reset</div>
            </div>

            {/* Display result if available */}
            <div style={{
                display: result ? 'block' : 'none'
            }}>
                {
                    JSON.stringify(result) // Display the result as JSON
                }
            </div>
        </div>
    );
}

export default Predict;
