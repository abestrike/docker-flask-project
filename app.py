from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Flask inside Docker!</h1>
    <p>This is my first Dockerized Python web app.</p>
    """

@app.route("/health")
def health():
    return {"status": "ok", "app": "docker-flask-project"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
