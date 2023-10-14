# db_connector.py

import mysql.connector
import logging

class DBConnector:
    def __init__(self, host, user, password, database):
        self.db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

        # Configure logging to log errors to a file and print them to the console
        logging.basicConfig(filename='.data/logs/sql_connection.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        logging.getLogger().addHandler(console_handler)

        try:
            # Establish the database connection during initialization
            self.db_connection = mysql.connector.connect(**self.db_config)
        except mysql.connector.Error as err:
            error_message = "Error connecting to the database: " + str(err)
            logging.error(error_message)
            print(error_message)

    def get_connection(self):
        return self.db_connection

    def close_connection(self):
        if self.db_connection:
            self.db_connection.close()
            print("Closed db Connection")

# Use your appropriate db credentials here
"""
db = DBConnector(
    host="localhost",
    user="njoroge",
    password="Student@db12",
    database="ovs_student"
)
"""
