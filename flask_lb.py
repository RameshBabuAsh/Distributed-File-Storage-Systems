from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Define the addresses and ports of your Flask servers
FLASK_SERVERS = [
    "http://localhost:5000",
    "http://localhost:5001"
    # Add more servers if needed
]

# Dictionary to track the load on each server
SERVER_LOAD = {server: 0 for server in FLASK_SERVERS}

class LoadBalancerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Choose the server with the lowest load
        chosen_server = min(FLASK_SERVERS, key=lambda server: SERVER_LOAD[server])
        
        # Update the load for the chosen server
        SERVER_LOAD[chosen_server] += 1
        
        # Forward the request to the chosen Flask server
        response = requests.get(chosen_server + self.path, stream=True)
        
        # Send the response back to the client
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
        self.end_headers()
        
        # Send the file content to the client
        for chunk in response.iter_content(chunk_size=1024):
            self.wfile.write(chunk)

    def do_POST(self):
        # Choose the server with the lowest load
        chosen_server = min(FLASK_SERVERS, key=lambda server: SERVER_LOAD[server])
        
        # Update the load for the chosen server
        SERVER_LOAD[chosen_server] += 1
        
        # Read the request body as bytes
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Forward the request to the chosen Flask server
        response = requests.post(chosen_server + self.path, data=post_data, headers=self.headers)
        
        # Send the response back to the client
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
        self.end_headers()
        self.wfile.write(response.content)

def run_load_balancer(server_class=HTTPServer, handler_class=LoadBalancerHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Load balancer running on port http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_load_balancer()
