# home.py

"""
    Homme Route defining route directories
"""

from http.server import SimpleHTTPRequestHandler
from http.cookies import SimpleCookie


class Home:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        # add logging

    def HandleStudentHome(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/student_home.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def HandleDelegate(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/student_home.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def HandleAdmin(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/admin_home.html", "rb") as file:
            self.request_handler.wfile.write(file.read())

    def HandlePollingOfficer(self):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", "text/html")
        self.request_handler.end_headers()
        with open("templates/po-home.html", "rb") as file:
            self.request_handler.wfile.write(file.read())
