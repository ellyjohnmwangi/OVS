# login.py

"""
    This package contains all handlers for the login
    It imports the db_connector and initiates it's own db connection does it's logic then closse it up
"""

import os
import sys
import http.cookies

path = os.path.abspath("../")
sys.path.append(path)
import utils
from modules.db_connector import DBConnector
from modules.authenticator import Authenticator


class LoginHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.db = DBConnector(
            host="localhost",
            user="root",
            password="",
            database="ovs_student"
        )
        self.auth = Authenticator(self.db.get_connection())

    def handle_get_student(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/student_login.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def handle_get_user(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/user_login.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def handle_authenticate_student(self):
        # Handle the authentication logic for student login
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length).decode("utf-8")
        post_params = {param.split("=")[0]: param.split("=")[1] for param in post_data.split("&")}
        email = post_params.get("email")
        password = post_params.get("password")
        print(f"[-] Student email {email} password {password}")
        auth_result = self.auth.authenticate_student(email, password)
        if auth_result is not None and auth_result[0]:  # Check if authentication succeeded
            _, student_id, department = auth_result
            print(f"[+] Authenticated student with id {student_id} from department {department}")
            # generate token and set as header
            token = utils.CreateStudentJWTToken(student_id, department)
            # Create a Cookie object and set the token as a cookie
            cookies = http.cookies.SimpleCookie()
            cookies["token"] = token
            # Get the cookie header as a string
            cookie_header = cookies.output(header="", sep="; ")
            self.request_handler.send_response(302)  # Redirect response code
            self.request_handler.send_header("Location", "/")  # Redirect URL
            self.request_handler.send_header("Content-type", "text/html")
            # Set the "Set-Cookie" header
            self.request_handler.send_header("Set-Cookie", cookie_header)
            self.request_handler.end_headers()
        else:
            self.request_handler.send_response(400)  # Bad request header
            self.request_handler.send_header("Content-type", "text/html")
            self.request_handler.end_headers()
            error_message = "Wrong username or password provided."
            # Load the HTML content from the file
            with open("templates/student_login.html", "rb") as file:
                html_content = file.read().decode("utf-8")
                # Inject the error message into the HTML content
                html_content = html_content.replace("{{wrong_password_provided}}", error_message)
                # Send the modified HTML content as the response
                self.request_handler.wfile.write(html_content.encode())


    def handle_authenticate_user(self):
        # Handle the authentication logic for admin login
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length).decode("utf-8")
        post_params = {param.split("=")[0]: param.split("=")[1] for param in post_data.split("&")}
        email = post_params.get("email")
        password = post_params.get("password")
        auth_result = self.auth.authenticate_user(email, password)
        if auth_result is not None and auth_result[0]:
            _, user_id, email, user_type = auth_result
            print(f"[+] User authenticated as {user_type} with admin ID {user_id}")
            # create a JWT token and set it as a cookie value
            token = utils.CreateUserJWTToken(user_id, user_type, email)
            # Create a Cookie object and set the token as a cookie
            cookies = http.cookies.SimpleCookie()
            cookies["token"] = token
            # Get the cookie header as a string
            cookie_header = cookies.output(header="", sep="; ")
            self.request_handler.send_response(302)  # Redirect response code
            self.request_handler.send_header("Location", "/adminhome")  # Redirect URL
            self.request_handler.send_header("Content-type", "text/html")
            # Set the "Set-Cookie" header
            self.request_handler.send_header("Set-Cookie", cookie_header)
            self.request_handler.end_headers()
        else:
            self.request_handler.send_response(400)  # Bad request header
            self.request_handler.send_header("Content-type", "text/html")
            self.request_handler.end_headers()
            error_message = "Wrong username or password provided."
            # Load the HTML content from the file
            with open("templates/user_login.html", "rb") as file:
                html_content = file.read().decode("utf-8")
                # Inject the error message into the HTML content
                html_content = html_content.replace("{{wrong_password_provided}}", error_message)
                # Send the modified HTML content as the response
                self.request_handler.wfile.write(html_content.encode())
