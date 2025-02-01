from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model(features):
    X = features.drop('label', axis=1)
    y = features['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Ensure the model directory exists
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/random_forest_model.pkl')
    
    return model
