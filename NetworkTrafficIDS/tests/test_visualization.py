import pandas as pd
import matplotlib.pyplot as plt

# Dummy data for testing the visualization
results = pd.Series([0, 0, 1, 0, 1, 0, 0, 0, 1, 0])

# Visualization function
def plot_results(results):
    plt.plot(results.index, results.values)
    plt.title('Intrusion Detection Results')
    plt.xlabel('Index')
    plt.ylabel('Detection Output')
    plt.show()

# Test the visualization function
plot_results(results)
