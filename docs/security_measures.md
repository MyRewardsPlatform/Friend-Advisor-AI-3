# Security Measures

This document outlines the security measures implemented in the Friend Advisor Score (FAST) system. The system is designed with a strong focus on security to ensure the protection of user data and maintain user privacy.

## Secure Configuration

The system uses environment variables to store sensitive configuration data, such as database credentials, blockchain private keys, and API keys. This is done using the `dotenv` package, which loads environment variables from a `.env` file into `process.env`. This file is not included in the version control system, preventing accidental exposure of sensitive data.

```python
# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_CONFIG = {
    'DB_NAME': os.getenv('DB_NAME'),
    'DB_USER': os.getenv('DB_USER'),
    'DB_PASSWORD': os.getenv('DB_PASSWORD'),
    'DB_HOST': os.getenv('DB_HOST'),
    'DB_PORT': os.getenv('DB_PORT')
}

# Blockchain configuration
BLOCKCHAIN_CONFIG = {
    'BLOCKCHAIN_PROVIDER': os.getenv('BLOCKCHAIN_PROVIDER'),
    'BLOCKCHAIN_PRIVATE_KEY': os.getenv('BLOCKCHAIN_PRIVATE_KEY'),
    'BLOCKCHAIN_ADDRESS': os.getenv('BLOCKCHAIN_ADDRESS')
}

# AI/ML model configuration
AI_MODEL_CONFIG = {
    'MODEL_PATH': os.getenv('MODEL_PATH')
}

# API configuration
API_CONFIG = {
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET')
}

# Security configuration
SECURITY_CONFIG = {
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'ENCRYPTION_ALGORITHM': os.getenv('ENCRYPTION_ALGORITHM')
}

# Frontend configuration
FRONTEND_CONFIG = {
    'FRONTEND_URL': os.getenv('FRONTEND_URL')
}
```

## Database Security

The system uses the `psycopg2` library to interact with the PostgreSQL database. Connections to the database are managed using a connection pool, which helps to prevent SQL injection attacks by using parameterized queries.

```python
# database.py

def execute_query(self, query, params=None):
    conn = self.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        self.release_connection(conn)
```

## Blockchain Security

The system uses the `web3` library to interact with the Ethereum blockchain. Transactions are signed locally using the private key, which is stored securely as an environment variable and never exposed.

```python
# blockchain.py

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

## User Authentication

User passwords are hashed using the `werkzeug.security` library before being stored in the database. The system uses JSON Web Tokens (JWT) for user authentication. The JWT secret key is stored securely as an environment variable.

```python
# auth.py

def __init__(self, username, password):
    self.username = username
    self.password = generate_password_hash(password)
```

## API Security

The system uses the `flask_jwt_extended` library to protect API endpoints. The `jwt_required` decorator is used to ensure that a valid JWT is provided with each request.

```python
# api.py

@app.route('/api/score', methods=['GET'])
@jwt_required
def get_score():
    username = get_jwt_identity()
    score = ScoreUpdate.get_score(username)
    return jsonify({'score': score}), 200
```

## Frontend Security

The frontend uses HTTPS for secure communication. User data is never stored in the frontend, and all sensitive operations are performed in the backend.

```javascript
// frontend/home.js

axios.get('/api/score', {
    headers: {
        'Authorization': `Bearer ${token}`
    }
})
```
