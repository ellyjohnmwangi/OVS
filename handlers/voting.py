import json
import logging
from mysql.connector import IntegrityError
from modules.db_connector import DBConnector


class VoteHandler:
    def __init__(self):
        self.db_connector = DBConnector()
        self.db_connection = self.db_connector.get_connection()

    def has_user_voted(self, student_id):
        try:
            with self.db_connection.cursor() as cursor:
                select_query = "SELECT * FROM votes WHERE student_id = %s"
                cursor.execute(select_query, (student_id,))
                result = cursor.fetchone()
                cursor.close()
                logging.info(result)
        except Exception as e:
            logging.error(e)
            logging.error(f"Error updating vote count: {str(e)}")
            return {"message": f"Internal Server Error: {str(e)}"}

        return bool(result)

    def insert_vote(self, student_id, candidate_id):
        with self.db_connection.cursor() as cursor:
            insert_query = "INSERT INTO votes (student_id, candidate_id) VALUES (%s, %s)"
            cursor.execute(insert_query, (student_id, candidate_id))
            self.db_connection.commit()

    def handle_vote_count(self, student_id, candidate_id):
        try:
            if self.has_user_voted(student_id):
                return {"status": "error", "message": "You have already voted. Multiple votes are not allowed."}
            with self.db_connection.cursor() as cursor:
                update_query = "UPDATE candidates SET vote_count = vote_count + 1 WHERE candidate_id = %s"
                cursor.execute(update_query, (candidate_id,))
                self.db_connection.commit()
            self.insert_vote(student_id, candidate_id)

            return {"status": "success", "message": "Vote counted successfully"}
        except IntegrityError as integrity_error:
            return {"status": "error", "message": "You have already voted. Multiple votes are not allowed."}
        except Exception as e:
            logging.error(e)
            logging.error(f"Error updating vote count: {str(e)}")
            return {"status": "error", "message": f"Internal Server Error: {str(e)}"}

    def get_candidates_votes(self):
        try:
            with self.db_connection.cursor() as cursor:
                select_query = """
                    SELECT c.candidate_id, s.first_name AS candidate_name, c.vote_count
                    FROM candidates c
                    JOIN students s ON c.student_id = s.student_id
                """
                cursor.execute(select_query)
                results = cursor.fetchall()

                candidates_votes = {}
                for candidate_id, candidate_name, vote_count in results:
                    candidates_votes[candidate_id] = {"candidate_name": candidate_name, "vote_count": vote_count}

                return {"status": "success", "candidates_votes": candidates_votes}
        except Exception as e:
            logging.error(e)
            return {"status": "error", "message": f"Internal Server Error: {str(e)}"}

    def get_response(self, result_message):
        json_response = json.dumps(result_message)
        encoded_response = json_response.encode('utf-8')
        return encoded_response
