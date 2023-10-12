from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import os

# Specify the directory where static files are located
STATIC_DIR = "/static"


class StaticFileHandler(BaseHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.directory = None

    def do_GET(self):
        if self.path == '/':
            # Serve "index.html" from the "templates" folder
            try:
                with open(os.path.join("templates", "index.html"), 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File Not Found')
        elif self.path.startswith('/static/'):
            # Serve static files
            self.serve_static_file()
        else:
            # Handle other routes
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
    def do_POST(self):
        if self.path.startswith('/static/'):
            # Create or update static files
            self.create_or_update_static_file()
        else:
            # Handle other routes
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_DELETE(self):
        if self.path.startswith('/static/'):
            # Delete static files
            self.delete_static_file()
        else:
            # Handle other routes
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def serve_static_file(self):
        try:
            path = os.path.join(STATIC_DIR, self.path.lstrip('/'))
            with open(path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File Not Found')

    def create_or_update_static_file(self):
        try:
            path = os.path.join(STATIC_DIR, self.path.lstrip('/'))
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            with open(path, 'wb') as file:
                file.write(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'File Created/Updated')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())

    def delete_static_file(self):
        try:
            path = os.path.join(STATIC_DIR, self.path.lstrip('/'))
            os.remove(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'File Deleted')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, StaticFileHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()

