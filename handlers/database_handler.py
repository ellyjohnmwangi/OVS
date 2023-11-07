# database_handler.py
import json
from modules.db_connector import DBConnector


def get_candidates_data():
    db_connector = DBConnector()
    connection = db_connector.get_connection()
    cursor = connection.cursor()

    select_query = "SELECT candidate_id, candidate_name, position FROM candidates"
    cursor.execute(select_query)
    candidate_data = cursor.fetchall()

    cursor.close()
    db_connector.close_connection()

    # Convert the data to a list of dictionaries
    candidates = [{"candidate_id": candidate[0], "candidate_name": candidate[1], "position": candidate[2]} for candidate
                  in candidate_data]

    return json.dumps(candidates)
