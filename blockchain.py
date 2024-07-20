# blockchain.py

from web3 import Web3
from config import BLOCKCHAIN_CONFIG

class Blockchain:
    def __init__(self):
        self.provider = BLOCKCHAIN_CONFIG['BLOCKCHAIN_PROVIDER']
        self.private_key = BLOCKCHAIN_CONFIG['BLOCKCHAIN_PRIVATE_KEY']
        self.address = BLOCKCHAIN_CONFIG['BLOCKCHAIN_ADDRESS']
        self.web3 = Web3(Web3.HTTPProvider(self.provider))

    def is_connected(self):
        return self.web3.isConnected()

    def get_balance(self):
        return self.web3.eth.getBalance(self.address)

    def send_transaction(self, to_address, value):
        nonce = self.web3.eth.getTransactionCount(self.address)
        gasEstimate = self.web3.eth.estimateGas({"from": self.address, "to": to_address, "value": value})

        transaction = {
            'from': self.address,
            'to': to_address,
            'value': value,
            'gas': gasEstimate,
            'gasPrice': self.web3.eth.gasPrice,
            'nonce': nonce,
            'chainId': 3
        }

        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)

blockchain_instance = Blockchain()
