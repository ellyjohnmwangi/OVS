import http
import json
import os, sys
from http.server import SimpleHTTPRequestHandler
from http.cookies import SimpleCookie

from handlers import login
from handlers.login import LoginHandler
from handlers.database_handler import CandidateHandler
from handlers.home import Home
from handlers.voting import VoteHandler
from utils.utils import Helpers as hps
import logging

logging.basicConfig(filename='server.log', level=logging.INFO)

path = os.path.abspath("../")
sys.path.append(path)

BLACKLISTED_TOKENS = set()

class Router(SimpleHTTPRequestHandler):
    isVotingOn = True

    def do_GET(self):
        if self.path == "/":
            print("Home path requested...")
            self.home_route()
        elif self.path == "/login":
            login_handler = LoginHandler(self)
            login_handler.handle_get_student()
        elif self.path == "/register-student":
            login_handler = LoginHandler(self)
            login_handler.handle_register_student()
        elif self.path == "/get-candidates":
            try:
                candidate_handler = CandidateHandler()
                candidates_data = candidate_handler.get_candidates_data()
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(candidates_data.encode('utf-8'))
            except Exception as e:
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
        elif self.path == "/get-votes":
            vote_handler = VoteHandler()
            candidates_votes_result = vote_handler.get_candidates_votes()
            json_response = json.dumps(candidates_votes_result)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_response.encode('utf-8'))
        elif self.path == "/vote":
            if not self.check_authentication():
                return
            else:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("templates/student_voting.html", "rb") as file:
                    self.wfile.write(file.read())
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
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            json_data = json.loads(post_data)
            student_id = json_data.get('student_id')
            candidate_id = json_data.get('candidate_id')
            vote_handler = VoteHandler()
            result_message = vote_handler.insert_vote(student_id=student_id, candidate_id=candidate_id)
            print(f"Response from server: {vote_handler.get_response(result_message)}")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(vote_handler.get_response(result_message).encode('utf-8'))
        elif self.path.startswith("/vote/"):
            if not self.check_authentication():
                return
            else:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                json_data = json.loads(post_data)
                user_id = self.get_id_from_request()
                student_id = self.get_id_from_request()
                candidate_id = json_data.get('candidate_id')
                vote_handler = VoteHandler()
                try:
                    result_message = vote_handler.handle_vote_count(student_id, candidate_id)
                    response = vote_handler.get_response(result_message)
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(response)
                except Exception as e:
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
        cookie_header = self.headers.get('Cookie')
        print(f'Cookie Header: {cookie_header}')
        cookie = SimpleCookie(cookie_header)
        print("Parsed Cookies:")
        for key, morsel in cookie.items():
            print(f"{key}: {morsel.value}")
        student_id = cookie.get('student_id').value if 'student_id' in cookie else None
        login_handler = LoginHandler(self)
        token = login.get_main_token(student_id, department='')
        print(f'get here: {token} student_id: {student_id}')
        return token

    def get_id_from_request(self):
        cookie = SimpleCookie(self.headers.get('Cookie'))
        student_id = cookie.get('student_id').value if 'student_id' in cookie else None
        return student_id

    def is_user_logged_in(self):
        token = self.get_token_from_request()
        if token in BLACKLISTED_TOKENS:
            return False
        if token:
            return True
        else:
            return False

    def check_authentication(self):
        if not self.is_user_logged_in():
            self.redirect_to_login()
            return False
        return True

    def redirect_to_login(self):
        print(f"[DEBUG] Redirecting to /login")
        self.send_response(303)
        self.send_header("Location", "/login")
        self.end_headers()

    def handle_logout(self):
        cookie_header = self.headers.get('Cookie')
        cookie = http.cookies.SimpleCookie(cookie_header)
        student_id = self.get_id_from_request()
        get_short_token = LoginHandler(self)
        short_token = get_short_token.get_short_lived_token(student_id)
        short_lived_token = cookie.get('short_lived_token').value if 'short_lived_token' in cookie else None
        print(f'Short_token: {short_token}')
        print(f'Short_livedtoken: {short_lived_token}')
        BLACKLISTED_TOKENS.add(short_token)
        print(f'blacklist{BLACKLISTED_TOKENS}')
        self.send_response(302)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", f"token=; expires=Thu, 01 Jan 1970 00:00:00 GMT")
        self.send_header("Set-Cookie", f"short_lived_token=; expires=Thu, 01 Jan 1970 00:00:00 GMT")
        self.end_headers()
        self.send_response(302)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT")
        self.end_headers()

    def home_route(self):
        print("I am at home")
        token = self.get_token_from_request()
        print("I have token.")
        if token is None:
            self.send_response(303)
            self.send_header("Location", "/login")
            self.end_headers()
            return
        elif type(token) is str:
            print(f"[+] Token is {token}")
            home = Home(self)
            payload = hps.ValidateJWTToken(token)
            if payload is not None:
                if 'user_type' in payload:
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
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    with open("templates/student_login.html", "rb") as file:
                        self.wfile.write(file.read())
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("templates/student_login.html", "rb") as file:
                    self.wfile.write(file.read())
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/student_login.html", "rb") as file:
                self.wfile.write(file.read())
