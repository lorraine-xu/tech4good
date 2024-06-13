# util/db_operations.py

import psycopg2
from config.db_config import DB_CONFIG

def get_connection():
    conn = psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    return conn

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_data(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()

def read_data():
    conn = get_connection()
    cur = conn.cursor()
    with open('sql/sample_query.sql', 'r') as file:
        query = file.read()
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

if __name__ == "__main__":
    create_table()
    insert_data('Alice', 30)
    insert_data('Bob', 25)
    data = read_data()
    for row in data:
        print(row)
