# auth.py

import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from database import db_instance
from config import SECURITY_CONFIG

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def save_to_db(self):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        params = (self.username, self.password)
        db_instance.execute_query(query, params)

    @staticmethod
    def find_by_username(username):
        query = "SELECT * FROM users WHERE username = %s"
        params = (username,)
        result = db_instance.fetch_query(query, params)
        if result:
            return User(result[0][1], result[0][2])
        return None

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expires_in=3600):
        return jwt.encode(
            {'id': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)},
            SECURITY_CONFIG['SECRET_KEY'], algorithm=SECURITY_CONFIG['ENCRYPTION_ALGORITHM']).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, SECURITY_CONFIG['SECRET_KEY'], algorithms=[SECURITY_CONFIG['ENCRYPTION_ALGORITHM']])
        except:
            return None
        return User.find_by_username(data['id'])

