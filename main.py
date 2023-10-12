import http.server
import socketserver

# Define the server parameters
ip_address = "127.0.0.1"
port = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

try:
    # Create the server
    with socketserver.TCPServer((ip_address, port), MyHandler) as http:
        print(f"Serving at {ip_address}:{port}")
        print("Press Ctrl+C to quit.")
        
        # Start the server
        http.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")
except Exception as e:
    print(f"Error: {e}")

