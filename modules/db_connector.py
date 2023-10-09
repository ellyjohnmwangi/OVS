# db_connector.py

import mysql.connector
import logging

# Configure logging to log errors to a file and print them to the console
logging.basicConfig(filename='.data/logs/sql_connection.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
logging.getLogger().addHandler(console_handler)

# Replace these values with your actual database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'student_db2'
}

try:
    # Establish the database connection when the module is imported
    db_connection = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    error_message = f"Error connecting to the database: {err}"
    logging.error(error_message)
    print(error_message)

# Export the connection
def get_db_connection():
    return db_connection


# Use your appropriate db credentials
"""
host="localhost",
user="njoroge",
password="Student@db12",
database="student_db2"
"""
