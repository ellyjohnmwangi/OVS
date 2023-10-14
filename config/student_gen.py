"""
    Generates both user and student data
    Before running this script incide this directory. change the logging directory at modules/db_connector.py to '../.data/logs/sql_connection.log'
"""

import csv
import faker
import mysql.connector
import os
import sys

path = os.path.abspath("../")
sys.path.append(path)

from modules.db_connector import DBConnector
from modules.student import Student
from modules.users import Users

fake = faker.Faker()
num_records = 10

db = DBConnector(
    host="localhost",
    user="root",
    password="",
    database="ovs_student"
)

cnct = db.get_connection()

def generate_and_insert_students(num_records, cursor):
    student = Student(cursor)

    student_data = []  # To store student data

    for _ in range(num_records):
        department = fake.random_element(elements=('SCM', 'SBE', 'SCCD'))
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.user_name() + "@student.cuk.ac.ke"  # Append the desired suffix
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

        result = student.CreateStudent(department, first_name, last_name, email, password)
        student_data.append([department, first_name, last_name, email, password])

        print(result)

    # Save student data to a CSV file
    with open('student_records.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['department', 'first_name', 'last_name', 'email', 'password'])
        writer.writerows(student_data)

# Generate and insert student records and save to CSV
generate_and_insert_students(num_records, cnct)

def generate_and_insert_users(num_records, cursor):
    users = Users(cursor)

    users_data = []  # To store user data

    for _ in range(num_records):
        email = fake.user_name() + "@student.cuk.ac.ke"  # Append the desired suffix
        user_type = fake.random_element(elements=('delegate', 'admin', 'polling_officer'))
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

        result = users.CreateUser(email, user_type, password)
        users_data.append([email, user_type, password])

        print(result)

    # Save user data to a CSV file
    with open('user_records.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['email', 'user_type', 'password'])
        writer.writerows(users_data)

# Generate and insert user records and save to CSV
generate_and_insert_users(num_records, cnct)

# Close the connection
cnct.close()
