import json
from modules.db_connector import DBConnector


class CandidateHandler:
    def __init__(self):
        self.db_connector = DBConnector()

    def get_candidates_data(self):
        connection = self.db_connector.get_connection()
        cursor = connection.cursor()

        select_query = "SELECT candidate_id, position_id, department FROM candidates"
        cursor.execute(select_query)
        candidate_data = cursor.fetchall()

        cursor.close()
        self.db_connector.close_connection()

        # Convert the data to a list of dictionaries
        candidates = [{"candidate_id": candidate[0], "position_id": candidate[1], "department": candidate[2]} for
                      candidate in candidate_data]


        return json.dumps(candidates)
