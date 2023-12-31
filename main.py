"""
    Main acts as the entry point for the whole project
    It only calls the router and serves the as per the port
"""

# import required files
import http.server
import http.server
import os
import socketserver
import sys

from handlers import router

path = os.path.abspath("./handlers")
sys.path.append(path)
PORT = 8000
IsVottingOn = False


class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run_server():
    handler = http.server.SimpleHTTPRequestHandler
    with MyTCPServer(("", PORT), router.Router) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
