# Docker Flask Project

This is my first Dockerized Python Flask web app.

## Project structure

```text
docker-flask-project/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## What this project does

- Runs a small Flask web app
- Has a home page at `/`
- Has a health check endpoint at `/health`
- Runs inside a Docker container

## Docker commands

Build the image:

```bash
docker build -t docker-flask-project .
```

Run the container:

```bash
docker run -d --name flask-web -p 5000:5000 docker-flask-project
```

Stop and remove the container:

```bash
docker stop flask-web
docker rm flask-web
```

Check running containers:

```bash
docker ps
```

Open in browser:

```text
http://localhost:5000
http://localhost:5000/health
```

## What I learned

- Flask is a small Python web framework.
- `requirements.txt` stores Python dependencies.
- Dockerfile tells Docker how to build the app image.
- `docker build` creates an image.
- `docker run` starts a container from that image.
- `-p 5000:5000` connects laptop port 5000 to container port 5000.
