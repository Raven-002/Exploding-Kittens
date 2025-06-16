from flask import Flask, render_template, send_from_directory
import socket
import threading
import os

app = Flask(__name__, static_folder='../../client/frontend/public', template_folder='../../client/frontend/public')

# Placeholder for C GameServer connection
C_SERVER_HOST = '127.0.0.1'
C_SERVER_PORT = 12345

def connect_to_c_server():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((C_SERVER_HOST, C_SERVER_PORT))
        print(f"Connected to C GameServer at {C_SERVER_HOST}:{C_SERVER_PORT}")
        # Placeholder for communication logic
        # client_socket.sendall(b"Hello from Python client!")
        # response = client_socket.recv(1024)
        # print(f"Received from C server: {response.decode()}")
        client_socket.close()
    except ConnectionRefusedError:
        print(f"Could not connect to C GameServer at {C_SERVER_HOST}:{C_SERVER_PORT}. Make sure it's running.")
    except Exception as e:
        print(f"An error occurred while connecting to C server: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/connect_server')
def api_connect_server():
    # This is a simplified example. In a real app, you'd manage persistent connections.
    threading.Thread(target=connect_to_c_server).start()
    return {"message": "Attempting to connect to C server..."}

@app.route('/<path:filename>')
def serve_static(filename):
    # This route serves static files from the public directory
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # In a production environment, use a WSGI server like Gunicorn
    app.run(debug=True, port=5000)
