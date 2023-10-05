import bcrypt
import mysql.connector
import csv


# Function to register a new student
def register_students_from_csv(csv_file):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="njoroge",
            password="Student@db12",
            database="student_db2"
        )
        cursor = connection.cursor()

        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email']
                password = row['password']

                # Generate a salt and hash the password
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

                # Insert student data into the database
                sql = "INSERT INTO students (first_name, last_name, email, hashed_password) VALUES (%s, %s, %s, %s)"
                values = (first_name, last_name, email, hashed_password.decode('utf-8'))
                cursor.execute(sql, values)
                connection.commit()

        print(f"Registration from {csv_file} successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


csv_file = 'student_records.csv'
register_students_from_csv(csv_file)
