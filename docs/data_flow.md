# Data Flow Documentation

This document describes the data flow in the Friend Advisor Score (FAST) system. The system leverages various technologies including AI/ML, blockchain, and a robust backend to assess and validate social authenticity.

## Overview

The data flow in the FAST system can be broadly divided into the following steps:

1. User Registration and Authentication
2. Data Collection and Processing
3. Score Calculation and Update
4. Score Retrieval and Display

## Detailed Data Flow

### User Registration and Authentication

The process begins with the user registration. The user's credentials are stored securely in the database. The password is hashed before storage for security purposes. This is handled by the `auth.py` module.

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
```

### Data Collection and Processing

Once the user is registered and authenticated, the system starts collecting and processing the user's online activities. The data is fetched from various sources like social media platforms and communication channels. The data is then processed and stored in the database. This is handled by the `database.py` module.

```python
class Database:
    def execute_query(self, query, params=None):
        conn = self.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
```

### Score Calculation and Update

The processed data is then fed into the AI/ML model for score calculation. The model analyzes the user's online presence and behavior to calculate a trustworthiness score. This score is then updated in the database in real-time. This is handled by the `ai_model.py` and `score_update.py` modules.

```python
class SocialAuthenticityModel(nn.Module):
    def __init__(self):
        super(SocialAuthenticityModel, self).__init__()
        # Define your model architecture here
        # This is just a placeholder
        self.layer1 = nn.Linear(100, 50)
        self.layer2 = nn.Linear(50, 10)
        self.layer3 = nn.Linear(10, 1)
```

### Score Retrieval and Display

Finally, the user's score is retrieved from the database and displayed on the frontend. The score is also stored on the blockchain for transparency and security. This is handled by the `blockchain.py` and `frontend/*.js` modules.

```python
class Blockchain:
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
```

## Conclusion

The data flow in the FAST system is designed to be efficient and secure. It ensures that the user's data is handled securely and the trustworthiness score is calculated accurately and updated in real-time.
