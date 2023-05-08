import http.server
import socketserver

# Reserve a port for the server to run
port = int(input("Enter server port: "))

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    active_connections = 0
    healthy = True
    
    def do_GET(self):
        if self.path == '/connections':
            # Response: Number of active connections to the server
            message = f"{RequestHandler.active_connections}"
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message.encode()))
            self.end_headers()
            self.wfile.write(message.encode())
        elif self.path == '/healthcheck':
            # Response: Health status of the server
            if RequestHandler.healthy:
                message = f"Server {port} is healthy"
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message.encode()))
                self.end_headers()
                self.wfile.write(message.encode())
            else:
                message = f"Server {port} is unhealthy"
                self.send_response(503)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message.encode()))
                self.end_headers()
                self.wfile.write(message.encode())
        else:
            # Response: Port number of the server
            message = f"This is server {port}"
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message.encode()))
            self.end_headers()
            self.wfile.write(message.encode())

    def log_message(self, format, *args):
        RequestHandler.active_connections += 1
        super().log_message(format, *args)
        RequestHandler.active_connections -= 1

# Start the server
with socketserver.TCPServer(("", port), RequestHandler) as httpd:
    print(f"Server running on port {port}")
    httpd.serve_forever()

