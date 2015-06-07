import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('Hello World!')

    def log_request(self, code): 
        # Disable console logging
        pass

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    handler_class = MyHandler
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

