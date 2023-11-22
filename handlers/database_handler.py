import json
from modules.db_connector import DBConnector


class CandidateHandler:
    def __init__(self):
        self.db_connector = DBConnector()

    def get_candidates_data(self):
        connection = self.db_connector.get_connection()
        cursor = connection.cursor()

        select_query = """
        SELECT
            c.candidate_id,
            s.first_name AS candidate_name,
            c.position_id,
            p.name_of_position,
            c.department
        FROM candidates c
        JOIN students s ON c.student_id = s.student_id
        JOIN positions p ON c.position_id = p.position_id;
        """
        cursor.execute(select_query)
        candidate_data = cursor.fetchall()

        cursor.close()

        # Convert the data to a list of dictionaries
        candidates = [
            {
                "candidate_id": candidate[0],
                "candidate_name": candidate[1],
                "position_id": candidate[2],
                "position_name": candidate[3],
                "department": candidate[4]
            }
            for candidate in candidate_data
        ]

        return json.dumps(candidates)

    def get_student_id(self, email):
        connection = self.db_connector.get_connection()
        cursor = connection.cursor()

        select_student_id_query = "SELECT student_id FROM students WHERE email = %s;"
        cursor.execute(select_student_id_query, (email,))
        student_id = cursor.fetchone()

        cursor.close()
        self.db_connector.close_connection()

        # Extract student ID from the result
        student_id = student_id[0] if student_id else None

        return student_id

    def get_dept(self, email):
        connection = self.db_connector.get_connection()
        cursor = connection.cursor()
        select_student_id_query = "SELECT department FROM students WHERE email = %s;"
        cursor.execute(select_student_id_query, (email,))
        department = cursor.fetchone()

        cursor.close()
        self.db_connector.close_connection()

        # Extract student ID from the result
        department = department[0] if department else None

        return department
