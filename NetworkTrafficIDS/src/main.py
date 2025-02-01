import os
from src import traffic_capture, feature_extraction, model_training, intrusion_detection, visualization

def main():
    print("Starting Network Traffic Analysis and Intrusion Detection System...")
    
    # Capture network traffic
    capture_file = traffic_capture.capture_traffic()
    
    # Check if the capture file has any content
    if os.path.getsize(capture_file) == 0:
        print("No data captured. Please check the network interface and try again.")
        return
    
    # Extract features from captured traffic
    features = feature_extraction.extract_features(capture_file)
    
    # Check if features DataFrame is empty
    if features.empty:
        print("No packets captured during feature extraction.")
        return
    
    # Print the features DataFrame to verify
    print(features.head())
    
    # Train the model
    print("Training the model...")
    model = model_training.train_model(features)
    print("Model training completed.")
    
    # Detect intrusions
    print("Detecting intrusions...")
    results = intrusion_detection.detect_intrusions(model, features)
    print("Intrusion detection completed.")
    
    # Visualize results
    print("Visualizing results...")
    visualization.plot_results(results)
    print("Process completed.")

if __name__ == "__main__":
    main()
