import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running.")

def start_dummy_server():
    server = HTTPServer(('0.0.0.0', 8080), DummyHandler)
    server.serve_forever()

threading.Thread(target=start_dummy_server).start()
