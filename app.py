from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import psycopg2
from config.db_config import DB_CONFIG
import logging

app = Flask(__name__)
# Enable CORS for your frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

logging.basicConfig(level=logging.DEBUG)


def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.form
        logging.debug(f"Received registration data: {data}")
        username = data['username']
        password = data['password']
        email = data['email']

        conn = get_connection()
        cur = conn.cursor()

        # Check if the user already exists
        cur.execute(
            "SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cur.fetchone()

        if existing_user:
            cur.close()
            conn.close()
            logging.debug("User already exists")
            return jsonify({'status': 'error', 'message': 'User already exists'}), 400

        # Insert the new user
        cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                    (username, password, email))
        conn.commit()
        cur.close()
        conn.close()

        logging.debug("User registered successfully")
        return jsonify({'status': 'success', 'message': 'User registered successfully'}), 200
    except Exception as e:
        logging.error(f"Error during registration: {e}")
        return jsonify({'status': 'error', 'message': 'An error occurred. Please try again.'}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.form
        logging.debug(f"Received login data: {data}")
        username = data['username']
        password = data['password']

        conn = get_connection()
        cur = conn.cursor()

        # Verify the user
        cur.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            logging.debug("Login successful")
            return jsonify({'status': 'success', 'message': 'Login successful'}), 200
        else:
            logging.debug("Invalid credentials")
            return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401
    except Exception as e:
        logging.error(f"Error during login: {e}")
        return jsonify({'status': 'error', 'message': 'An error occurred. Please try again.'}), 500


@app.route('/login.html')
def login_page():
    return render_template('login.html')


@app.route('/register.html')
def register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
