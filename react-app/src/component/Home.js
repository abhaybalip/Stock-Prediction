
import '../asset/style/Home.css'

const Home = () => {
    return (
        <div className='app-main-home'>
            <div className='hm-p1'>
                <h2 className='p1-title'>About the project ...</h2>
                <div className='p1-txt'>
                    <span>Welcome to our website, a platform dedicated to providing insightful stock market predictions.</span>
                    <span>Our mission is to empower investors with data-driven forecasts to make informed decisions.</span>
                </div>
            </div>

            <div className='hm-p2'>
                <h2 className='p2-title'>Problem Statement : </h2>
                <div className='p2-txt'>
                    <span>Navigating the stock market can be complex. We aim to simplify this process by offering predictive analytics.</span>
                    <span>Many investors struggle with market volatility. We provide tools to help mitigate risk.</span>
                </div>
            </div>

            <div className='hm-p3'>
                <h2 className='p3-title'>Methodology & Technology</h2>
                <div className='p3-txt'>
                    <span>Our predictive models leverage advanced techniques, including LSTM neural networks, ARIMA time-series analysis, and linear regression.</span>
                    <span>We analyze historical stock data and market trends, processing them through these algorithms to generate insightful forecasts.</span>
                    <span>These models are continuously refined and tested to enhance accuracy and adapt to dynamic market conditions.</span>
                    <span>We focus on providing data-driven predictions, acknowledging the inherent uncertainties of financial markets.</span>
                </div>
            </div>

            <div className='hm-p4'>
                <h2 className='p4-title'>Disclaimer & Risk (Essential for Compliance)</h2>
                <div className='p4-txt'>
                    <span>Please note that stock market predictions are inherently uncertain, and past performance is not indicative of future results.</span>
                    <span>Our predictions should not be considered financial advice.</span>
                    <span>We recommend consulting with a qualified financial advisor before making any investment decisions.</span>
                </div>
            </div>
        </div>
    )
}
export default Home;
