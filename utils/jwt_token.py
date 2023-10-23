import jwt  # You may need to install the 'PyJWT' library
import datetime


class CreateStudentJWTToken:
    @staticmethod
    def create(student_id, department):
        payload = {
            'student_id': student_id,
            'department': department,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expiration time
        }
        secret_key = 'your_secret_key'  # Replace with your secret key
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token


class CreateUserJWTToken:
    @staticmethod
    def create(user_id, user_type, email):
        payload = {
            'user_id': user_id,
            'user_type': user_type,
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expiration time
        }
        secret_key = 'your_secret_key'  # Replace with your secret key
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token
