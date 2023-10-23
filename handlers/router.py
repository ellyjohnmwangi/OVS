# router.py
import os, sys
from http.server import SimpleHTTPRequestHandler
from http.cookies import SimpleCookie

path = os.path.abspath("../")
sys.path.append(path)

from handlers.login import LoginHandler
from handlers.home import Home
from utils.utils import Helpers as hps

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

    def get_token_from_request(self):
        # Extract the token from the request's cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        token = cookie.get('token').value if 'token' in cookie else None
        return token

    def home_route(self):
        #  @TODO IMPLEMENT LOGIC FOR CHEcKING IF VOTTED IR IF TIME TO VOTE BLAH BLAH
        # get token from request and print it out.
        token = self.get_token_from_request()
        if token:
            print(f"[+] Token is {token}")
            # call home
            home = Home(self,token)
            payload = hps.ValidateJWTToken(token)
            match payload.user_type:
                case "student_id":
                    home.HandleStudentHome()
                case "delegate":
                    home.HandleDelegate()
                case "polling_officer":
                    home.HandlePollingOfficer()
                case "admin":
                    home.HandleAdmin()
        else:
            #redirect to login
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/student_login.html", "rb") as file:
                self.wfile.write(file.read())


"""
    tokenUserTypes = 'student,admin,delegate,polling_officer
    class HomePage:
        # check if user has logged in
            if not Lg In
        # if user has logged in, get token and unmarshal the payload
            # if student
                check if voted
                    if voted, redirect to results page
                if not voted
                    check if voting is on:
                        if on: redirect to voting
                        if not: redirect to results
            # if user:
                if delegate: check if delegate voting is on
                    if on: let them vote
                    if not: redirect to results page
                if admin:
                    redirect to admin page
                if polling officer:
                    # they should have a polling officer admin page or something

"""
