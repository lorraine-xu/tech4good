# util/db_operations.py

import psycopg2
from config.db_config import DB_CONFIG

"""
Establishes and returns connection to the PostgreSQL db using the
configuration details from DB_CONFIG.

Returns:
    psycopg2.connection: A connection obj to the PostgreSQL db.
"""
def get_connection():
    conn = psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    return conn

"""
Creates the table 'test_table' in PostgreSQL db;
    it includes the following: id, name, and age.
"""
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

"""
Inserts a new record into the 'test_table' in the PostgreSQL db.

Args: 
    name (str): name inserted.
    age (int): age inserted.
"""
def insert_data(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()

"""
Reads and returns all records from the 'test_table' in the PostgreSQL database.

Returns:
    list of tuple: A list of tuples where each tuple represents a row in the 'test_table'.
"""
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

# Database Test
if __name__ == "__main__":
    # Create the table if it doesn't exist
    create_table()

    # Insert dummy data into the table
    insert_data('Alice', 30)
    insert_data('Bob', 25)

    # Read and pritn all data from the table
    data = read_data()
    for row in data:
        print(row)
