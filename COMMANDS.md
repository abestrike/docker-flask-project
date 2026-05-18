# Docker Flask Project Commands

## Local workflow

```bash
cd ~/projects/docker-flask-project
docker stop flask-web
docker rm flask-web
docker build -t docker-flask-project .
docker run -d --name flask-web -p 5000:5000 \
  -e APP_ENV=local \
  -e APP_VERSION=1.2.0 \
  docker-flask-project
curl http://localhost:5000/version
docker logs flask-web
