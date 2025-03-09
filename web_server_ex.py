import http.server
import socketserver
import mimetypes

PORT = 9010
DIRECTORY = "/path/to/hls"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".m3u8"):
            self.send_header("Content-Type", "application/vnd.apple.mpegurl")
        elif self.path.endswith(".ts"):
            self.send_header("Content-Type", "video/MP2T")
        super().end_headers()

handler = CustomHandler
handler.directory = DIRECTORY

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving HLS on port {PORT}")
    httpd.serve_forever()
