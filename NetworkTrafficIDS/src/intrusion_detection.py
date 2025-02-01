import joblib

def detect_intrusions(model, features):
    model = joblib.load('model/random_forest_model.pkl')
    predictions = model.predict(features.drop('label', axis=1))
    return predictions
