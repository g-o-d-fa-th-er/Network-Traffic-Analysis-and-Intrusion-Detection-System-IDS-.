import unittest
from src.intrusion_detection import detect_intrusions

class TestIntrusionDetection(unittest.TestCase):
    def test_detect_intrusions(self):
        # Provide sample model and features for testing
        model = ...  # Replace with actual model or mock
        features = ...  # Replace with actual features or mock
        results = detect_intrusions(model, features)
        self.assertIsNotNone(results)

if __name__ == "__main__":
    unittest.main()
