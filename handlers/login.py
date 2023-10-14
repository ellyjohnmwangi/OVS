# login.py

"""
    This package contains all handlers for the login
    It imports the db_connector and initiates it's own db connection does it's logic then closse it up
"""

import os
import sys

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
        with open("templates/login.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def handle_get_user(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/admin_login.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def handle_authenticate_student(self):
        # Handle the authentication logic for student login
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length).decode("utf-8")
        post_params = {param.split("=")[0]: param.split("=")[1] for param in post_data.split("&")}
        email = post_params.get("email")
        password = post_params.get("password")
        result = self.auth.authenticate_student(email, password)
        if result:
            self.request_handler.send_response(200)
            self.request_handler.send_header("Content-type", "text/html")
            self.request_handler.end_headers()
            with open("templates/index.html", "rb") as file:
                self.request_handler.wfile.write(file.read())
        else:
            # Handle authentication failure (e.g., send an error message or redirect)
            pass

    def handle_authenticate_user(self):
        # Handle the authentication logic for admin login
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length).decode("utf-8")
        post_params = {param.split("=")[0]: param.split("=")[1] for param in post_data.split("&")}
        email = post_params.get("email")
        password = post_params.get("password")
        success, user_type, admin_id = authenticator.authenticate_user(email, password)
        if success:
            print(f"User authenticated as {user_type} with admin ID {admin_id}")
            # create a jwt token as and write it as a cookie value
            token = utils.CreateJWTToken(user_type,admin_id)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/admin.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            #write wrong credentials
            pass
