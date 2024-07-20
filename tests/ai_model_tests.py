# tests/ai_model_tests.py

import unittest
import torch
from ai_model import AIModel, SocialAuthenticityModel

class TestSocialAuthenticityModel(unittest.TestCase):
    def setUp(self):
        self.model = SocialAuthenticityModel()

    def test_forward_pass(self):
        # Create a random tensor of size [1, 100]
        input_tensor = torch.randn(1, 100)
        output = self.model(input_tensor)
        # Check if the output is a tensor
        self.assertIsInstance(output, torch.Tensor)
        # Check if the output tensor has the correct size
        self.assertEqual(output.size(), (1, 1))

class TestAIModel(unittest.TestCase):
    def setUp(self):
        self.ai_model = AIModel()

    def test_model_loading(self):
        # Check if the model is loaded correctly
        self.assertIsInstance(self.ai_model.model, SocialAuthenticityModel)

    def test_prediction(self):
        # Create a random tensor of size [1, 100]
        user_data = [0.5]*100
        prediction = self.ai_model.predict(user_data)
        # Check if the prediction is a float
        self.assertIsInstance(prediction, float)

if __name__ == '__main__':
    unittest.main()
