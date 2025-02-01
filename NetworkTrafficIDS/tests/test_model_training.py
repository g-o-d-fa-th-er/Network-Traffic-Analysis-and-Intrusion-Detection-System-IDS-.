import unittest
from src.model_training import train_model
import pandas as pd

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        # Provide sample features as input
        data = {'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'label': [0, 1, 0]}
        features = pd.DataFrame(data)
        model = train_model(features)
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()
