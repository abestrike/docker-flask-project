from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <h1>Hello from Flask inside Docker!</h1>
    <p>This is my first Dockerized Python web app.</p>
    <p>App version: {APP_VERSION}</p>
    """

@app.route("/health")
def health():
    return {"status": "ok", "app": "docker-flask-project"}

@app.route("/version")
def version():
    return {"version": APP_VERSION}

@app.route("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
