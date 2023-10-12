# voting_utils.py

import hashlib
from mysql.connector import connect


def hash_vote(student_id, term_id, candidate_id, position_id):
    # Combine the details into a single string
    vote_data = f"{student_id}-{term_id}-{candidate_id}-{position_id}"

    # Create a hash object (you can choose the hash algorithm, e.g., SHA-256)
    hash_object = hashlib.sha256()

    # Update the hash object with the combined data
    hash_object.update(vote_data.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_vote = hash_object.hexdigest()

    return hashed_vote


# define a connection object
        host="localhost",
        user="njoroge",
        password="Student@db12",
        database="student_db2")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for r in result:
        print(r)
    cursor.close()
    conn.close()
    # print('A connection object has been created.')

    # close the database connection
    conn.close()


connexion('select * from students;')
