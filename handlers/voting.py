import json
import logging

from mysql.connector import IntegrityError

from modules.db_connector import DBConnector


class VoteHandler:
    def __init__(self):
        self.db_connector = DBConnector()
        self.db_connection = self.db_connector.get_connection()

    def has_user_voted(self, user_id):
        try:

            with self.db_connection.cursor() as cursor:
                select_query = "SELECT * FROM votes WHERE student_id = %s"
                cursor.execute(select_query, (user_id,))
                result = cursor.fetchone()
                cursor.close()
                logging.info(result)
        except Exception as e:
            # Log other exceptions with details
            logging.error(e)
            logging.error(f"Error updating vote count: {str(e)}")
            return {"message": f"Internal Server Error: {str(e)}"}

        return bool(result)

    def insert_vote(self, student_id, candidate_id):
        with self.db_connection.cursor() as cursor:
            # Insert the vote into the votes table
            insert_query = "INSERT INTO votes (student_id, candidate_id) VALUES (%s, %s)"
            cursor.execute(insert_query, (student_id, candidate_id))
            self.db_connection.commit()

    def handle_vote_count(self, student_id, candidate_id):
        try:
            # Check if the user has already voted
            if self.has_user_voted(student_id):
                return {"status": "error", "message": "You have already voted. Multiple votes are not allowed."}

            # Connect to the database and update the vote count
            #         connection = self.db_connector.get_connection()
            #         cursor = connection.cursor()
            # Connect to the database and update the vote count
            with self.db_connection.cursor() as cursor:
                # Update the vote count for the specified candidate_id
                update_query = "UPDATE candidates SET vote_count = vote_count + 1 WHERE candidate_id = %s"
                cursor.execute(update_query, (candidate_id,))
                self.db_connection.commit()

            # Insert the vote into the votes table to track the user's vote
            self.insert_vote(student_id, candidate_id)

            return {"status": "success", "message": "Vote counted successfully"}
        except IntegrityError as integrity_error:
            # Handle the case where the user has already voted
            return {"status": "error", "message": "You have already voted. Multiple votes are not allowed."}
        except Exception as e:
            # Log other exceptions with details
            logging.error(e)
            logging.error(f"Error updating vote count: {str(e)}")
            return {"status": "error", "message": f"Internal Server Error: {str(e)}"}


    def get_response(self, result_message):
        # Convert the result_message dictionary to a JSON-encoded string
        json_response = json.dumps(result_message)
        # Encode the JSON string to bytes using UTF-8
        encoded_response = json_response.encode('utf-8')
        return encoded_response
