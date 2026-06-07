from flask import Flask
import socket
from datetime import datetime
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "local")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return f"""
    <h1>Hello from Flask inside Docker!</h1>
    <p>This is my Dockerized Python Flask web app.</p>
    <p>Environment: {APP_ENV}</p>
    <p>App version: {APP_VERSION}</p>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "app": "docker-flask-project",
        "environment": APP_ENV
    }

@app.route("/version")
def version():
    return {
        "version": APP_VERSION,
        "environment": APP_ENV
    }

@app.route("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": APP_ENV
    }
