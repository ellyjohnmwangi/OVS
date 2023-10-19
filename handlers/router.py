# router.py
import os, sys
from http.server import SimpleHTTPRequestHandler

path = os.path.abspath("../")
sys.path.append(path)

from handlers.login import LoginHandler

"""
    Our good route only accepts two methods, a GET and and POST request
"""


class Router(SimpleHTTPRequestHandler):
    """
    # setting new global variables
    # check if voting is on:
    """
    isVotingOn = True

    def do_GET(self):
        if self.path == "/":
            self.home_route()
        # Login handles
        # Adding register for debugging purposes
        elif self.path == "/register-student":
            login_handler = LoginHandler(self)
            login_handler.handle_register_student()
        elif self.path == "/login":
            login_handler = LoginHandler(self)
            login_handler.handle_get_student()
        elif self.path == "/admin":
            login_handler = LoginHandler(self)
            login_handler.handle_get_user()
        elif self.path == "/vote":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/vote.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            # Serve static files
            if self.path.endswith(".css"):
                content_type = "text/css"
            elif self.path.endswith(".js"):
                content_type = "application/javascript"
            elif self.path.endswith(".jpg") or self.path.endswith(".jpeg"):
                content_type = "image/jpeg"
            else:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.wfile.write(b"404 Page Not Found")
                return

            try:
                with open("." + self.path, "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", content_type)
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 File Not Found")

    def do_POST(self):
        if self.path == "/login":
            login_handler = LoginHandler(self)
            login_handler.handle_authenticate_student()
        elif self.path == "/admin":
            login_handler = LoginHandler(self)
            login_handler.handle_authenticate_user()
        elif self.path == "/register-student":
            login_handler = LoginHandler(self)
            login_handler.handle_student_registration()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Page Not Found")

    def home_route(self):
        #  @TODO IMPLEMENT LOGIC FOR CHEKING IF VOTTED IR IF TIME TO VOTE BLAH BLAH
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("templates/index.html", "rb") as file:
            self.wfile.write(file.read())
