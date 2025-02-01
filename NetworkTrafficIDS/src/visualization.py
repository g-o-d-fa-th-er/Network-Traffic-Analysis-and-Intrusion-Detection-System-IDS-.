import matplotlib.pyplot as plt

def plot_results(results):
    plt.plot(range(len(results)), results)
    plt.title('Intrusion Detection Results')
    plt.xlabel('Index')
    plt.ylabel('Detection Output')
    
    # Save the plot as an image file
    plt.savefig('output/intrusion_detection_results.png')
    
    # Also display the plot
    plt.show()
