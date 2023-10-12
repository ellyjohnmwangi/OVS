import http.server
import socketserver

PORT = 8000  # You can change the port number as needed


# Define a custom handler to disable caching (for development purposes)
class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()


# Create an HTTP server
with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    print(f"Serving at port {PORT}")

    try:
        # Serve the current directory
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
