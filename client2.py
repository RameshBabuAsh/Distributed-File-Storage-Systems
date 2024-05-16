from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

LOAD_BALANCER_HOST = "localhost"
LOAD_BALANCER_PORT = 9000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filepath = f"uploads/{file.filename}"
        file.save(filepath)
        response = send_request(f"upload {filepath}")
        return response
    return "No file provided"

@app.route('/download', methods=['POST'])
def download():
    filename = request.form['filename']
    if filename:
        response = send_request(f"download {filename}")
        return response
    return "No filename provided"

def send_request(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((LOAD_BALANCER_HOST, LOAD_BALANCER_PORT))
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

if __name__ == '__main__':
    app.run(debug=True, port=3002)
