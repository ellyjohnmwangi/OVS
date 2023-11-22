import logging
import mysql.connector

class Candidate:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def create_candidate(self, student_id, position_id):
        try:
            insert_query = "INSERT INTO candidates (student_id, position_id) VALUES (%s, %s)"
            self.cursor.execute(insert_query, (student_id, position_id))
            self.db_connection.commit()
            return "Candidate created successfully"
        except mysql.connector.Error as err:
            error_message = f"Error creating candidate: {err}"
            logging.error(error_message)
            return error_message

    def candidate_exists(self, student_id, position_id):
        # Check if the candidate already exists for the specified position
        existing_candidate_query = "SELECT * FROM candidates WHERE student_id = %s AND position_id = %s"
        self.cursor.execute(existing_candidate_query, (student_id, position_id))
        existing_candidate = self.cursor.fetchone()
        return bool(existing_candidate)

def add_candidate(student_id, position_id):
    # Assuming you have a db_connection object (database connection) already created
    db_connection = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )

    # Create a Candidate instance
    candidate_handler = Candidate(db_connection)

    try:
        # Check if the candidate already exists
        if not candidate_handler.candidate_exists(student_id, position_id):
            # If the candidate doesn't exist, create a new candidate
            creation_result = candidate_handler.create_candidate(student_id, position_id)
            print(creation_result)
        else:
            print("Candidate already exists for this position.")
    finally:
        # Close the database connection
        db_connection.close()
