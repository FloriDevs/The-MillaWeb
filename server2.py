from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            try:
                with open('index.txt', 'r') as file:
                    content = file.readlines()
                    response_content = ""
                    for line in content:
                        if line.startswith("Link:"):
                            link = line.split("Link: ")[1].strip()
                        elif line.startswith("LinkName:"):
                            link_name = line.split("LinkName: ")[1].strip()
                            response_content += f"{link_name}: {link}\n"
                        else:
                            response_content += line  # Füge normalen Text hinzu
                    self.wfile.write(response_content.encode('utf-8'))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'404 Not Found: index.txt not found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    # Lokale IP-Adresse ermitteln
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f'Starting server on:')
    print(f'  - Local: http://localhost:{port}')
    print(f'  - Local IP: http://{local_ip}:{port}')

    httpd.serve_forever()

if __name__ == "__main__":
    run()
