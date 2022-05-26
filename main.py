<<<<<<< Updated upstream
zdr
kak si
=======
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "r") as fd:
            self.wfile.write(bytes(fd.read(), "utf-8"))

        if self.path.startswith("/api"):
            if self.path == "/api/pastes" or self.path == "/api/pastes/":
                pass
            elif self.path.startswith("/api/pastes/"):
                pass
        else:
            if self.path == "/pastes" or self.path == "/pastes/":
                with open("create_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))
            elif self.path.startswith("/pastes/"):
                with open("read_paste.html", "r") as fd:
                    self.wfile.write(bytes(fd.read(), "utf-8"))
                    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
            
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        with open("request_body.txt", "w") as fd:
            fd.write(post_data.decode('utf-8'))



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
>>>>>>> Stashed changes
