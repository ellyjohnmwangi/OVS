# router.py
import os, sys
from http.server import SimpleHTTPRequestHandler
from http.cookies import SimpleCookie

from handlers.voting import VotingHandler

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
            print("Home path requested...")
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
            with open("templates/student_voting.html", "rb") as file:
                self.wfile.write(file.read())
        #This should be abstracted to handlePO class
        elif self.path == "/po":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/po-home.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/list-elections":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/list-elections.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/list-candidates":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/list-candidates.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/view-candidates":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/view-candidates.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/list-positions":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/list-positions.html", "rb") as file:
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
        if self.path == "/vote":
            # if voted:
            #     # User has already voted, redirect to the results page
            #     self.send_response(303)  # 303 See Other
            #     self.send_header("Location", "/results")
            #     self.end_headers()
            # else:
            #     # Handle the form submission
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode("utf-8")

            # Parse the form data (you may need to adjust this based on your form structure)
            form_data = {param.split('=')[0]: param.split('=')[1] for param in post_data.split('&')}

            # Extract relevant data from the form data (e.g., candidate_id, term_id, student_id)
            candidate_id = form_data.get('candidate_id')
            term_id = form_data.get('term_id')
            student_id = form_data.get('student_id')

            # Create an instance of VotingHandler
            voting_handler = VotingHandler()

            # Call a method in VotingHandler to update the database
            result_message = voting_handler.handle_vote(student_id, term_id, candidate_id)

            # Redirect to the results page
            self.send_response(303)  # 303 See Other
            self.send_header("Location", "/results")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Page Not Found")

    def get_token_from_request(self):
        # Extract the token from the request's cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        token = cookie.get('token').value if 'token' in cookie else None
        return token

    def handle_logout(self):
        # Invalidate the token on the server side (e.g., remove the session)
        # ...

        # Clear the token from the user's browser
        self.send_response(302)  # 302 Found (redirect)
        self.send_header("Location", "/login")  # Redirect to the login page
        self.send_header("Set-Cookie", "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT")  # Clear the token cookie
        self.end_headers()

    def home_route(self):
        print("I am at home")
        # @TODO IMPLEMENT LOGIC FOR CHECKING IF VOTED OR IF TIME TO VOTE BLAH BLAH
        # get token from request and print it out.
        token = self.get_token_from_request()
        print("I have token.")
        if token is None:
            # Token is missing, redirect to the login page
            self.send_response(303)
            self.send_header("Location", "/login")
            self.end_headers()
            return
        elif type(token) is str:
            print(f"[+] Token is {token}")
            # call home
            home = Home(self)
            payload = hps.ValidateJWTToken(token)
            if payload is not None:
                if 'user_type' in payload:  # Check if 'user_type' exists in the payload dictionary
                    user_type = payload['user_type']
                    print(f"Usertype is: {user_type}")
                    match user_type:
                        case "student":
                            home.handle_student_home()
                        case "delegate":
                            home.handle_delegate()
                        case "polling_officer":
                            home.handle_polling_officer()
                        case "admin":
                            home.handle_admin()
                else:
                    # Handle the case where 'user_type' is not present in the payload
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    with open("templates/student_login.html", "rb") as file:
                        self.wfile.write(file.read())
            else:
                # Handle the case where payload is None (invalid token)
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("templates/student_login.html", "rb") as file:
                    self.wfile.write(file.read())
        else:
            # Redirect to log in
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/student_login.html", "rb") as file:
                self.wfile.write(file.read())
