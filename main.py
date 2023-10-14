"""
    Main acts as the entry point for the whole project
    It only calls the router and serves the as per the port
"""

# import required files
import http.server
import socketserver
import os
import sys

# Initiate internal libraries for importing get_db_connection
#path = os.path.abspath("./modules")
#sys.path.append(path)

path = os.path.abspath("./handlers")
sys.path.append(path)

## initiate a DB Connection
# from db_connector import DBConnector
from router import Router

PORT = 8000

def run_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Router) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()


"""
def main():
    db = DBConnector(
        host="localhost",
        user="root",
        password="",
        database="ovs_student"
    )

    cnct = db.get_connection()
    if not cnct:
        print("Error connecting to DB, Check Logs")

    db.close_connection()

if __name__ == "__main__":
    main()
"""
