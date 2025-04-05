import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import io

def generate_graph(actual, predicted, algorithm_name, quote):
    # Plot actual vs predicted
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Actual Prices', color='blue')
    plt.plot(predicted, label='Predicted Prices', color='red')
    plt.title(f'{algorithm_name} - Predicted vs Actual Prices')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()

    # Create graph folder if needed
    os.makedirs('graph', exist_ok=True)
    path = f'graph/{quote}_{algorithm_name}.png'

    # Save plot to file
    plt.savefig(path)
    plt.close()
