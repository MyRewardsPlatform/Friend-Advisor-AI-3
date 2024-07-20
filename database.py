# database.py

import psycopg2
from psycopg2 import pool
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.db_pool = None

    def create_pool(self):
        self.db_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            database=DATABASE_CONFIG['DB_NAME'],
            user=DATABASE_CONFIG['DB_USER'],
            password=DATABASE_CONFIG['DB_PASSWORD'],
            host=DATABASE_CONFIG['DB_HOST'],
            port=DATABASE_CONFIG['DB_PORT']
        )

    def get_connection(self):
        if self.db_pool is None:
            self.create_pool()
        return self.db_pool.getconn()

    def release_connection(self, conn):
        if self.db_pool:
            self.db_pool.putconn(conn)

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

    def fetch_query(self, query, params=None):
        conn = self.get_connection()
        result = None
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchall()
        except Exception as e:
            print(f"Database error: {e}")
        finally:
            self.release_connection(conn)
        return result

db_instance = Database()
