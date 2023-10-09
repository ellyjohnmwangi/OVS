import http.server
import socketserver
# import SimpleHTTPServer

ip_address = "127.0.0.1"
port = 8000
Handler = http.server.SimpleHTTPRequestHandler
http = socketserver.TCPServer((ip_address, port), Handler)
print("Serving at port:", port)

http.serve_forever()
