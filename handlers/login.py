# login.py

"""
    This package contains all handlers for the login
    It imports the db_connector and initiates it's own db connection does it's logic then closse it up
"""

import http.cookies
import json
import os
import sys
from urllib.parse import unquote

import utils.logger
from handlers.voting import VoteHandler
from modules.authenticator import Authenticator
from modules.db_connector import DBConnector
from modules.student import Student
from utils.utils import Helpers as hps

path = os.path.abspath("../")
sys.path.append(path)
BLACKLISTED_TOKENS = set()


def get_main_token(student_id, department):
    # Generate the main token for the student
    token = hps.CreateStudentJWTToken(student_id, department)
    # Create a Cookie object and set the token as a cookie
    cookies = http.cookies.SimpleCookie()
    cookies["token"] = str(token)
    cookies["student_id"] = str(student_id)
    # Get the cookie header as a string
    cookie_header = cookies.output(header="", sep="; ")
    print(f' get main token: {token}')
    return token, cookie_header


class LoginHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.db = DBConnector()
        self.auth = Authenticator(self.db.get_connection())

        utils.logger.setup_logging("../.data/logs/auth_handler.log")

        # added student code to debug registration, remove this later :)

    def handle_register_student(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/register_student.html", "rb") as file:
            self.request_handler.wfile.write(file.read())


    def handle_student_registration(self):
        # initiate a new DB connection and and call Student class
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length).decode("utf-8")
        # Decode the URL-encoded POST data
        post_data = unquote(post_data)
        post_params = {param.split("=")[0]: param.split("=")[1] for param in post_data.split("&")}
        department = post_params.get("department")
        first_name = post_params.get("first-name")
        last_name = post_params.get("last-name")
        email = post_params.get("email")
        password = post_params.get("password")
        self.student = Student(self.db.get_connection())
        result = self.student.CreateStudent(department, first_name, last_name, email, password)
        if result != "Student created successfully":
            utils.logger.log_error("Failed to register student with email " + email)
            print(f"[-] Error registering student {result}")
        else:
            print("Registered student try logging in")
            self.request_handler.send_response(302)  # Redirect response code
            self.request_handler.send_header("Location", "/login")  # Redirect URL
            self.request_handler.send_header("Content-type", "text/html")
            self.request_handler.end_headers()
        self.student.CloseConnection()

    def handle_get_student(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/student_login.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def get_short_lived_token(self, student_id):
        # Generate the short-lived token for the student
        short_lived_token = hps.create_short_lived_token(student_id, expiration=3600)  # Set expiration time in seconds
        cookies = http.cookies.SimpleCookie()
        cookies["short_lived_token"] = str(short_lived_token)
        print(f'short_lived2{short_lived_token}')
        cookies["student_id"] = str(student_id)
        # Get the cookie header as a string
        cookie_header = cookies.output(header="", sep="; ")
        return short_lived_token, cookie_header

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
        post_params = {param.split("=")[0]: unquote(param.split("=")[1]) for param in post_data.split("&")}
        email = post_params.get("email")
        password = post_params.get("password")
        auth_result = self.auth.authenticate_student(email, password)
        if auth_result is not None and auth_result[0]:  # Check if authentication succeeded
            _, student_id, department = auth_result
            # print(f"Debug: Authenticated student_id: {student_id}")

            # Check if the student has voted
            vote_handler = VoteHandler()
            if vote_handler.has_user_voted(student_id):
                # User has voted, redirect to the dashboard
                short_lived_token = hps.create_short_lived_token(student_id, expiration=3600)
                cookies = http.cookies.SimpleCookie()
                cookies["short_lived_token"] = str(short_lived_token)
                cookies["student_id"] = str(student_id)
                print(f"short_lived_token: {short_lived_token}")

                self.request_handler.send_response(303)
                self.request_handler.send_header("Location", "/dashboard")
                self.request_handler.end_headers()
            else:
                # User hasn't voted, generate token and redirect to the voting page
                token = hps.CreateStudentJWTToken(student_id, department)
                # Create a Cookie object and set the token as a cookie
                cookies = http.cookies.SimpleCookie()
                cookies["token"] = str(token)
                cookies["student_id"] = str(student_id)
                print(f"Token after creating: {token}")

                # print(f"Debug: Redirecting to /vote with student_id: {student_id}")

                # Get the cookie header as a string
                cookie_header = cookies.output(header="", sep="; ")
                # Include student_id in the response data
                response_data = {
                    "message": "Authentication successful",
                    "student_id": student_id,
                }
                # Include a script block to store student_id in session storage
                script_block = f"""
                        <script>
                            sessionStorage.setItem("student_id", "{student_id}");
                            window.location.href = "/vote";  // Redirect to the voting page
                        </script>
                        """

                self.request_handler.send_response(200)  # OK response code
                self.request_handler.send_header("Content-type", "text/html")
                self.request_handler.send_header("Set-Cookie", cookie_header)
                self.request_handler.end_headers()

                # Send the modified response data and script block as HTML
                self.request_handler.wfile.write((json.dumps(response_data) + script_block).encode('utf-8'))

        else:
            utils.logger.log_error("Failed to authenticate student with email " + email)
            self.request_handler.send_response(400)  # Bad request header
            self.request_handler.send_header("Content-type", "text/html")
            self.request_handler.end_headers()
            error_message = "Wrong username or password provided."
            # Load the HTML content from the file
            with open("templates/student_response.html", "rb") as file:
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
            token = utils.utils.CreateUserJWTToken(user_id, user_type, email)
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
            with open("templates/user_response.html", "rb") as file:
                html_content = file.read().decode("utf-8")
                # Inject the error message into the HTML content
                html_content = html_content.replace("{{wrong_password_provided}}", error_message)
                # Send the modified HTML content as the response
                self.request_handler.wfile.write(html_content.encode())