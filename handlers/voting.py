import hashlib

from modules.db_connector import DBConnector


class VotingHandler:
    def __init__(self):
        # Create a DBConnector instance
        self.db_connector = DBConnector()

    def handle_vote(self, student_id, term_id, candidate_id, position_id):
        try:
            # Get the database connection
            connection = self.db_connector.get_connection()
            cursor = connection.cursor()

            # Check if the user has already voted
            check_vote_query = """
                SELECT voting_id
                FROM voting
                WHERE student_id = %s AND term_id = %s AND position_id = %s
            """
            cursor.execute(check_vote_query, (student_id, term_id, position_id))
            existing_vote = cursor.fetchone()

            if existing_vote:
                # User has already voted, handle accordingly
                return "You have already voted. Thank you!"

            # Update the candidate's vote count
            update_vote_count_query = """
                UPDATE candidates
                SET no_of_votes = no_of_votes + 1
                WHERE candidate_id = %s
            """
            cursor.execute(update_vote_count_query, (candidate_id,))
            connection.commit()

            # Generate a hash for auditing and verification
            vote_data = f"{student_id}:{term_id}:{candidate_id}:{position_id}".encode()
            hash_value = hashlib.sha256(vote_data).hexdigest()

            # Store the vote details in the voting table for auditing
            store_vote_query = """
                INSERT INTO voting (student_id, term_id, candidate_id, position_id, hash)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(store_vote_query, (student_id, term_id, candidate_id, position_id, hash_value))
            connection.commit()

            return "Your vote has been recorded. Thank you for voting!"

        except Exception as err:
            print(f"Error handling vote: {err}")
            return "An error occurred while processing your vote. Please try again later."

        finally:
            # Close the database connection
            cursor.close()
            self.db_connector.close_connection()


# Example usage:
# Replace the values with actual data from your application
# student_id = 1
# term_id = 1
# candidate_id = 2
# position_id = 3
#
# vote_handler = Vote()
# result_message = vote_handler.handle_vote(student_id, term_id, candidate_id, position_id)
# print(result_message)
