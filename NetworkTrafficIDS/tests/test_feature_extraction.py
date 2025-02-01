import unittest
from src.feature_extraction import extract_features

class TestFeatureExtraction(unittest.TestCase):
    def test_extract_features(self):
        capture_file = 'data/capture.pcap'
        features = extract_features(capture_file)
        self.assertIsNotNone(features)

if __name__ == "__main__":
    unittest.main()
