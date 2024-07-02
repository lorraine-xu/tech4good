# vue-project

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

---

# Tech4Good Web Application

Tech4Good is a web application designed to support and promote sustainable practices. This project includes a Flask backend and a Vue.js frontend, and it uses PostgreSQL as the database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Node.js and npm installed
- PostgreSQL installed
- pgAdmin installed (optional, for database management)

## Installation

### Backend Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/tech4good.git
   cd tech4good/backend
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `config/db_credentials.py` file with your database credentials:

   ```python
   # config/db_credentials.py
   DB_USER = 'your_db_user'
   DB_PASSWORD = 'your_db_password'
   ```

5. Update the database configuration in `config/db_config.py` if necessary:

   ```python
   # config/db_config.py
   from .db_credentials import DB_USER, DB_PASSWORD

   DB_CONFIG = {
       'host': 'localhost',
       'port': '5432',
       'database': 'tech4good',
       'user': DB_USER,
       'password': DB_PASSWORD
   }
   ```

### Database Setup in pgAdmin 4

1. **Open pgAdmin 4**:

   - Launch pgAdmin 4 from your installed applications.

2. **Set a Master Password**:

   - When prompted, set a master password to secure and manage your connections.

3. **Add a New Server**:

   - Click on "Add New Server" in the pgAdmin dashboard.
   - **General Tab**:
     - Name: Enter a name for your server connection (e.g., "Local PostgreSQL").
   - **Connection Tab**:
     - Hostname/Address: `localhost`
     - Port: `5432`
     - Maintenance Database: `postgres`
     - Username: `your_db_user` (Replace with your PostgreSQL username)
     - Password: `your_db_password` (Replace with your PostgreSQL password)
   - Click "Save" to add the new server connection.

4. **Create a New Database**:

   - Connect to your PostgreSQL server by clicking on the server name you just added.
   - Right-click on the "Databases" node under your server.
   - Select "Create" > "Database...".
   - **Database Name**: Enter `tech4good`.
   - **Owner**: Ensure it is set to your database user.
   - Click "Save".

5. **Create the `users` Table**:
   - Select the `tech4good` database from the list.
   - Navigate to the "Query Tool" from the Tools menu or by right-clicking the database and selecting "Query Tool".
   - Execute the following SQL command to create the `users` table:
     ```sql
     CREATE TABLE users (
         id SERIAL PRIMARY KEY,
         username VARCHAR(255) NOT NULL UNIQUE,
         password VARCHAR(255) NOT NULL,
         email VARCHAR(255) NOT NULL UNIQUE
     );
     ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```sh
   cd frontend/src
   ```

2. Install the required npm packages:
   ```sh
   npm install
   ```

## Running the Application

### Running the Backend

1. Ensure your virtual environment is activated:

   ```sh
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

2. Start the Flask application:
   ```sh
   python app.py
   ```

### Running the Frontend

1. Navigate to the frontend directory:

   ```sh
   cd src
   ```

2. Start the development server:

   ```sh
   npm run dev
   ```

3. Open your browser and go to `http://localhost:5173`.

## Usage

### Register a New User

1. Navigate to the registration page at `http://localhost:5173/register.html`.
2. Enter your email, username, and password.
3. Click "Register" to create a new account.

### Log In

1. Navigate to the login page at `http://localhost:5173/login.html`.
2. Enter your username and password.
3. Click "Login" to access your account.

## Contributing

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Vue.js](https://vuejs.org/)
- [PostgreSQL](https://www.postgresql.org/)

```

### Additional Notes:
- Replace `yourusername` with your actual GitHub username or the correct repository URL.
- Make sure to add the `requirements.txt` file for the Python dependencies if it does not already exist.
- Make sure the PostgreSQL server is running before starting the Flask application.

```
