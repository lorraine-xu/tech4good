import os
from flask import Flask, jsonify
import psycopg2
from config.config import Config

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=Config.PG_HOST,
        database=Config.PG_DATABASE,
        user=Config.PG_USER,
        password=Config.PG_PASSWORD
    )
    return conn

def get_query(filename):
    with open(os.path.join('sql', filename), 'r') as file:
        return file.read()

@app.route('/insert', methods=['POST'])
def insert():
    conn = get_db_connection()
    cur = conn.cursor()
    query = get_query('insert.sql')
    cur.execute(query, ('sample name',))
    conn.commit()
    cur.close()
    conn.close()
    return 'Inserted successfully', 201

@app.route('/read', methods=['GET'])
def read():
    conn = get_db_connection()
    cur = conn.cursor()
    query = get_query('read.sql')
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
