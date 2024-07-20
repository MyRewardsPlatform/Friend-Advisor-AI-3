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
