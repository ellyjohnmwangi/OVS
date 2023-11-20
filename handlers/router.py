import json
import os, sys
from http.server import SimpleHTTPRequestHandler
from http.cookies import SimpleCookie
from handlers.login import LoginHandler
from handlers.database_handler import CandidateHandler
from handlers.home import Home
from handlers.voting import VoteHandler
from utils.utils import Helpers as hps
import logging

logging.basicConfig(filename='server.log', level=logging.INFO)

path = os.path.abspath("../")
sys.path.append(path)

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
        elif self.path == "/get-candidates":
            try:
                # Create an instance of CandidateHandler
                candidate_handler = CandidateHandler()

                # Get candidates data as a JSON string
                candidates_data = candidate_handler.get_candidates_data()

                # Send HTTP response with candidates data
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(candidates_data.encode('utf-8'))
            except Exception as e:
                # Handle exceptions (e.g., database connection error)
                self.send_response(500)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Internal Server Error: {str(e)}".encode('utf-8'))

        elif self.path == "/admin":
            login_handler = LoginHandler(self)
            login_handler.handle_get_user()
        elif self.path == "/dashboard":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/dashboard.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/vote":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/student_voting.html", "rb") as file:
                self.wfile.write(file.read())
        # This should be abstracted to handlePO class
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
        # End of po GET routes
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
        elif self.path == "/logout":
            self.handle_logout()
        elif self.path == "/admin":
            login_handler = LoginHandler(self)
            login_handler.handle_authenticate_user()
        elif self.path == "/register-student":
            login_handler = LoginHandler(self)
            login_handler.handle_student_registration()
        elif self.path == "/update-vote/":
            # Extract the JSON data from the request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            json_data = json.loads(post_data)

            # Get student_id and candidate_id from the JSON data
            student_id = json_data.get('student_id')
            candidate_id = json_data.get('candidate_id')

            # Call the insert_vote method from VoteHandler
            vote_handler = VoteHandler()
            result_message = vote_handler.insert_vote(student_id=student_id, candidate_id=candidate_id)

            # Respond to the client with the JSON-encoded response
            print(f"Response from server: {vote_handler.get_response(result_message)}")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(vote_handler.get_response(result_message).encode('utf-8'))

        elif self.path.startswith("/vote/"):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            json_data = json.loads(post_data)
            student_id = json_data.get('student_id')
            candidate_id = json_data.get('candidate_id')
            vote_handler = VoteHandler()
            try:
                # Call the handle_vote_count method from VoteHandler
                result_message = vote_handler.handle_vote_count(student_id, candidate_id)

                response = vote_handler.get_response(result_message)

                # Respond to the client with the JSON-encoded response
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(response)
            except Exception as e:
                # Log the exception
                print(f"Exception in handle_vote_count: {str(e)}")
                self.send_response(500)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Internal Server Error: {str(e)}".encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Page Not Found")

    def get_token_from_request(self):
        # Extract the token from the request's cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        token = cookie.get('token').value if 'token' in cookie else None
        # student_id = cookie.get('student_id').value if 'student_id' in cookie else None

        return token

    def get_id_from_request(self):
        # Extract the token from the request's cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        student_id = cookie.get('student_id').value if 'student_id' in cookie else None

        return student_id

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

    """
        Main acts as the entry point for the whole project
        It only calls the router and serves the as per the port
    """


