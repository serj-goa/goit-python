import json
import mimetypes
import pathlib
import socket
import urllib.parse

from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000
BUFFER = 1024


def send_data_to_socket(body):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(body, (SERVER_IP, SERVER_PORT))
    client_socket.close()


class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        send_data_to_socket(body)

        body = urllib.parse.unquote_plus(body.decode())
        payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        new_data = {str(datetime.now()): payload}
        print(new_data)

        with open(BASE_DIR.joinpath('storage/data.json'), encoding='utf-8') as fd:
            json_file = fd.read()

            if not json_file:
                storage_data = {}
            else:
                storage_data = json.loads(json_file)

            storage_data.update(new_data)

        with open(BASE_DIR.joinpath('storage/data.json'), 'w', encoding='utf-8') as fd:
            json.dump(storage_data, fd, ensure_ascii=False)

        self.send_response(302)
        self.send_header('Location', 'index.html')
        self.end_headers()

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)

        match route.path:
            case '/':
                self.send_html('index.html')

            case '/message':
                self.send_html('message.html')

            case _:
                file = BASE_DIR / route.path[1:]

                if file.exists():
                    self.send_static(file)

                else:
                    self.send_html('error.html', 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        with open(filename, 'rb') as f:
            self.wfile.write(f.read())

    def send_static(self, filename):
        self.send_response(200)
        mime_type, *rest = mimetypes.guess_type(filename)

        if mime_type:
            self.send_header('Content-Type', mime_type)

        else:
            self.send_header('Content-Type', 'text/plain')

        self.end_headers()

        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())


def run(server=HTTPServer, handler=HTTPHandler):
    address = ('', 3000)
    http_server = server(address, handler)

    try:
        http_server.serve_forever()

    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    STORAGE_DIR = pathlib.Path().joinpath('storage')
    FILE_STORAGE = STORAGE_DIR / 'data.json'

    if not FILE_STORAGE.exists():
        with open(FILE_STORAGE, 'w') as fd:
            pass

    run()
