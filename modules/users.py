# users.py

"""
    Contains all user functions. More to be updated later
"""

import mysql.connector
import bcrypt
import logging

class Users:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()

    def CreateUser(self, email, user_type, password):
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            insert_query = "INSERT INTO users (email, user_type, password) VALUES (%s, %s, %s)"
            self.cursor.execute(insert_query, (email, user_type, hashed_password))
            self.db_connection.commit()
            return "User created successfully"
        except mysql.connector.Error as err:
            error_message = f"Error creating user: {err}"
            logging.error(error_message)
            return error_message

    def ChangePassword(self, user_id, new_password):
        # Hash the new password using bcrypt
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        try:
            update_query = "UPDATE users SET password = %s WHERE admin_id = %s"
            self.cursor.execute(update_query, (hashed_password, user_id))
            self.db_connection.commit()
            return "Password updated successfully"
        except mysql.connector.Error as err:
            error_message = f"Error updating password: {err}"
            logging.error(error_message)
            return error_message

    def ListUsers(self):
        try:
            select_query = "SELECT * FROM users"
            self.cursor.execute(select_query)
            users = []
            for row in self.cursor.fetchall():
                user = {
                    "admin_id": row[0],
                    "email": row[1],
                    "user_type": row[2],
                    "created_at": row[3],
                    "updated_at": row[4],
                }
                users.append(user)
            return users
        except mysql.connector.Error as err:
            error_message = f"Error listing users: {err}"
            logging.error(error_message)
            return error_message

    def ListUsersByType(self, user_type):
        try:
            select_query = "SELECT * FROM users WHERE user_type = %s"
            self.cursor.execute(select_query, (user_type,))
            users = []
            for row in self.cursor.fetchall():
                user = {
                    "admin_id": row[0],
                    "email": row[1],
                    "user_type": row[2],
                    "created_at": row[3],
                    "updated_at": row[4],
                }
                users.append(user)
            return users
        except mysql.connector.Error as err:
            error_message = f"Error listing users by user type: {err}"
            logging.error(error_message)
            return error_message

    def GetUserById(self, user_id):
        try:
            select_query = "SELECT * FROM users WHERE admin_id = %s"
            self.cursor.execute(select_query, (user_id,))
            row = self.cursor.fetchone()
            if row:
                user = {
                    "admin_id": row[0],
                    "email": row[1],
                    "user_type": row[2],
                    "created_at": row[3],
                    "updated_at": row[4],
                }
                return user
            else:
                return "User not found"
        except mysql.connector.Error as err:
            error_message = f"Error retrieving user by ID: {err}"
            logging.error(error_message)
            return error_message

    def CloseConnection(self):
        self.cursor.close()
        self.db_connection.close()
