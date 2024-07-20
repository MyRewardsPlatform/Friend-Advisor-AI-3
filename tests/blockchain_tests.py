# tests/blockchain_tests.py

import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_is_connected(self):
        self.assertTrue(self.blockchain.is_connected(), "Blockchain connection failed.")

    def test_get_balance(self):
        balance = self.blockchain.get_balance()
        self.assertIsInstance(balance, int, "Balance should be an integer.")
        self.assertGreaterEqual(balance, 0, "Balance should be greater than or equal to 0.")

    def test_send_transaction(self):
        initial_balance = self.blockchain.get_balance()
        to_address = '0x1234567890abcdef1234567890abcdef12345678'  # Dummy address for testing
        value = 1  # Sending 1 wei for testing

        # Send transaction and get transaction hash
        tx_hash = self.blockchain.send_transaction(to_address, value)
        self.assertIsInstance(tx_hash, str, "Transaction hash should be a string.")

        # Check if balance has decreased by at least the value sent
        # Note: In a real-world scenario, you would also need to account for gas fees
        final_balance = self.blockchain.get_balance()
        self.assertLessEqual(final_balance, initial_balance - value, "Balance did not decrease after transaction.")

if __name__ == '__main__':
    unittest.main()
