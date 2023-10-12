import mysql.connector
import bcrypt


# Function to authenticate a student
def authenticate_student(email, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="njoroge",
            password="Student@db12",
            database="student_db2"
        )
        cursor = connection.cursor()
        sql = "SELECT hashed_password FROM students WHERE email = %s"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
        if result:
            hashed_password = result[0].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                print("Authentication successful.")
            else:
                print("User not found!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


# Example usage:
authenticate_student("johndoe@example.com", "password123")
