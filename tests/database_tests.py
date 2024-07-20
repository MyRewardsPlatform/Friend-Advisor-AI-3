# tests/database_tests.py

import unittest
from database import Database, db_instance
from config import DATABASE_CONFIG
import psycopg2

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = db_instance
        self.db.create_pool()

    def tearDown(self):
        self.db.db_pool.closeall()

    def test_create_pool(self):
        self.assertIsNotNone(self.db.db_pool)

    def test_get_connection(self):
        conn = self.db.get_connection()
        self.assertIsInstance(conn, psycopg2.extensions.connection)
        self.db.release_connection(conn)

    def test_release_connection(self):
        conn = self.db.get_connection()
        self.db.release_connection(conn)
        self.assertEqual(self.db.db_pool._used, 0)

    def test_execute_query(self):
        query = "CREATE TABLE IF NOT EXISTS test_table (id serial PRIMARY KEY, num integer, data varchar);"
        self.db.execute_query(query)
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'test_table'")
        result = cur.fetchone()
        self.db.release_connection(conn)
        self.assertEqual(result[0], 1)

    def test_fetch_query(self):
        query = "INSERT INTO test_table (num, data) VALUES (%s, %s);"
        params = (100, 'testdata')
        self.db.execute_query(query, params)
        fetch_query = "SELECT * FROM test_table WHERE data = 'testdata';"
        result = self.db.fetch_query(fetch_query)
        self.assertEqual(result[0][1], 100)
        self.assertEqual(result[0][2], 'testdata')

if __name__ == '__main__':
    unittest.main()
