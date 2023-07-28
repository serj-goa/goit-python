import json
import pathlib
import urllib.parse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello world!</h1>
  </body>
</html>

"""


class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(html.encode())


def run(server=HTTPServer, handler=HTTPHandler):
    address = ('', 5555)
    http_server = server(address, handler)

    try:
        http_server.serve_forever()

    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    run()
