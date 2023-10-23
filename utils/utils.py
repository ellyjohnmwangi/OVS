#utils.py

"""
    This package explores utility functions to be used throught the project
"""

import re
import bcrypt
import html
import jwt
import datetime
import secrets
import string

SECRET_KEY = 'OVS'


class Helpers:
    # Email validation
    def IsValidEmail(email):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email) is not None

    # Password hashing and validation
    def HashPassword(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def ValidatePassword(input_password, hashed_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

    # User input sanitization
    def SanitizeUserInput(user_input):
        return html.escape(user_input)

    # JWT token creation and validation
    def CreateUserJWTToken(user_id, user_type,email):
        payload = {
            'email': email,
            'user_id': user_id,
            'user_type': user_type,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    def CreateStudentJWTToken(student_id, department):
        payload = {
            'student_id': student_id,
            'department': department,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    def ValidateJWTToken(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.DecodeError:
            return None

    def generate_random_string():
        random_string_length = secrets.randbelow(6) + 10
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(random_string_length))
