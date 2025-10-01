# Intro to Docker

## General
Docker creates and runs containers - software bundled to run on a minimal isolated linux OS on the host system.
Containers are great because they are typically very easy to install and even easier to uninstall.
Allows for reproducing environments, avoiding the "it runs on my machine" problem.
They can enhance security by isolating the host system from the system running the software.

Terms:

- Image: A copy of the software that is ready to run on docker.
- Container: An instance of an image, specific to the image that has been setup to run. More simply,
  a container is an image running on your machine. Can be turned on or off, etc.
- Volume: A path that a container can use to access host file system.

# Common Commands
```bash
# When you find an image you want to use do
docker pull <image_name>

# To see images downloaded use
docker images

# see running containers
docker ps

# see all containers
docker ps -a

# run a new container.
docker run image-name -d
# -d means run in detached mode so when the terminal is closed, the container continues to run

# run existing container 
docker start container-name

# stop docker container
docker stop image-name

# remove an image by name and tag
docker rmi postgres:latest

# remove a container by ID or name
docker rm 123456789abc
docker rm container_01

# Docker containers are their own sort of OS. You can SSH into it.
docker exec -it <container-name-or-id> /bin/sh
# /bin/sh is the terminal experience (shell in this case) you could do /bin/bash

# access container logs
docker logs <container name or id>

# continuously showing log output
docker logs -f <container-name-or-id>

```

## Run a Container Examples

```bash
# simplest docker image run
docker run hello-world

# run alpine linux (tiny image). sh lets you explore inside the container
docker run -it alpine sh

# Some containers need other info to run, which can be passed after the command
# --name is what the container will be named
# -p is for port mapping host computer port to image port (first is host, second is container)
# -e is for adding environment variables
docker run --name postgres_db -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

## Connecting Resources to Host

### Docker Ports

Accessing endpoints from the host machine is typically done through ports. You can map the
host machine port to the port that is being used in the docker container.

```docker run -p 5432:5432 -d <image_name>```

### Docker Volumes

Files and Docker
If you need to use files for anything involving docker, you need to configure volumes.

Volumes are a mapping of the docker container file system to the host file system.

``-v /home/svr/immich:/usr/src/app/upload``

Just like port mapping, the first is host and second is container.

## List of Flags

These are the ones you’ll use 90% of the time:

* `-d` → Run in **detached mode** (in the background).
* `-it` → Interactive + TTY (keeps a terminal open).
* `--name <name>` → Give your container a name.
* `-p <host:container>` → Publish ports (e.g., `-p 8080:80`).
* `-e <KEY=VALUE>` → Set environment variables.
* `-v <host:container>` → Mount a volume (bind mount or Docker volume).
* `--rm` → Automatically remove the container when it exits.
* `--network <network>` → Connect to a specific network.
* `--restart <policy>` → Restart policy (`no`, `always`, `on-failure`, `unless-stopped`).
* `--cpus`, `--memory` → Limit CPU/memory usage.
* `--entrypoint <command>` → Override the default entrypoint.
* `--workdir <dir>` → Set working directory inside the container.
* `--user <uid:gid>` → Run as a different user.
---

# Docker Compose

Docker compose is a handy way to run docker with configuration files.
This is nice when you have more complex containers to run, and its a difficult to type all the config
every time you want to run it.

*Important step:* Make sure you have the latest version (currently V2).

Docker compose V1 was built on python, V2 is built in Go. If you run ``which docker compose``
and it shows the path ``/usr/bin/docker-compose`` then you still have V1. Remove it
with ``sudo rm /usr/bin/docker-compose``.

Create a ``docker-compose.yaml`` file. Here's an example:

```yaml
services: # Defines the containers (services)
  app:
    image: my_flask_app:latest  # Use an existing image
    build: ..  # Or build from Dockerfile in the current directory
    ports:
      - "5000:5000"  # Map host port 5000 to container port 5000
    volumes:
      - ./app:/app  # Mount local folder to container folder
    environment:
      - FLASK_ENV=development  # Set environment variables
    depends_on:
      - db  # Wait for "db" service before starting

  db:
    image: postgres:15
    restart: always  # Restart if it crashes
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - pg_data:/var/lib/postgresql/data  # Persistent storage for DB

volumes:
  pg_data:  # Named volume for PostgreSQL data

```

Run container
``docker compose up -d``

Stop container
``docker compose down``

Upgrade container
``docker compose down``
``docker compose pull``
``docker compose up -d``

Restart container: ``docker compose restart``

Chain commands like ``docker compose down && docker compose up -d``


# Build a Docker Image

A **Dockerfile** is how to build an image. The contents might look something like this:

## Build Dockerfile

Simple python app:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Flask app (more complex):
```dockerfile
# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy app files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose the port (optional if using Docker Compose)
EXPOSE 8090

# Run Gunicorn when the container starts
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8090", "web_app.app:app"]
```

## Build Image

```bash
# build the image
docker build -t my-image-name:tag .  # <- don't forget that period

# example 1
docker build -t my-flask-app:latest .

# example 2
docker build -t my-flask-app:v1.0 .

# building on a Mac but will run on linux, specify to run on amd64.
docker build --platform linux/amd64 -t yt_download:latest .

# once the image has been created:
# save image to a tar file for sharing/copying
docker save -o /Users/tyleranderson/Downloads/yt_downloads_250226.tar yt_download:latest

# load the file as an image
docker load -i /srv/flask_yt_download/yt_downloads_250226.tar`
```

## Docker Compose with Custom Images

When you use docker compose with an image, you have two options:

Build image as part of docker compose start up.
```yaml
services:
  flask_app:
    build: .  # This tells Compose to use the Dockerfile in the current directory
    container_name: flask_gunicorn
    ports:
      - "8090:8090"

```

Run when image already exists.
```yaml
services:
  flask_app:
    image: my_flask_app  # Use the existing built image
    container_name: flask_gunicorn
    ports:
      - "8090:8090"
```

## Automating Build and Deploy

There are many steps when it comes to building and deploying. They can all be automated in one script.
Here's an example:

Dockerfile
```dockerfile
# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y curl

# Copy app files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose the port (optional if using Docker Compose)
EXPOSE 8090

# Run Gunicorn when the container starts
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8090", "app:app"]
```

Deployment script
```bash
#!/usr/bin/env bash

echo "Remove existing image to make a new one."
docker rmi yt_download:latest

rm data.db || echo "No db to remove, moving on"

echo "Build image for Linux server."
docker build --platform linux/amd64 -t yt_download:latest .  # uses Dockerfile to build
docker save -o yt_download_image.tar yt_download:latest

echo "Transfer file to server."
rsync -v --rsync-path="sudo rsync" yt_download_image.tar tyler@anderson.home:/srv/flask_yt_download

echo "Remove local copy of Docker image and docker image file."
docker rmi yt_download:latest
rm yt_download_image.tar

echo "Log into server and spin up image."
ssh tyler@anderson.home << 'EOF'
cd /srv/flask_yt_download || { echo "Directory not found"; exit 1; }

# create database file
sudo touch data.db

# Spin down container if running
sudo docker compose down || echo "No container running"

# Remove old Docker image
sudo docker rmi yt_download || echo "Image not found"

# Load new image
sudo docker load -i yt_download_image.tar

# Remove the transferred image file
sudo rm yt_download_image.tar

# Restart the container
sudo docker compose up -d
EOF
```

## Add uv to image

```dockerfile
# build a wheel file inside a docker image
FROM python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
```

## Multi-Stage build

You can build an image in stages.
It creates separate images during the build.
The last one that runs becomes the actual image.

```dockerfile
# Build stage
FROM python:3.13 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY . /src
WORKDIR /src
RUN uv build

# Runtime stage
FROM python:3.13-slim AS runtime
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY --from=builder /src/dist/*.whl && rm /tmp/*.whl

RUN uv pip install --system /tmp/*.whl && rm /tmp/*.whl

CMD ["invoice_start", "--sharepoint"]
```

# Ollama

Ollama is an open-source LLM runtime environment.

Simply put:

1. Rum Ollama
2. Download the model you'd like to use (mistral, llama3, etc.)
3. Go to the WebUI
4. Select the model you want to use.
5. Chat away!

Download a model: ``docker exec -it ollama ollama pull mistral`` or ``docker exec -it ollama ollama pull llama3``

Here is a docker compose file that runs it all:

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: unless-stopped
    ports:
      - "11434:11434"   # Ollama API exposed
    volumes:
      - ollama_data:/root/.ollama  # Persist models

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    restart: unless-stopped
    ports:
      - "3000:8080"   # WebUI runs here
    environment:
      - OLLAMA_API_BASE_URL=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:
```

You can go to [https://localhost:3000](https://localhost:3000) to use the web ui or you can use the API.

API call:

```http
### Generate text with llama3
POST http://localhost:11434/api/generate
Content-Type: application/json

{
  "model": "llama3",
  "prompt": "Write a haiku about data pipelines"
}
```

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": "Hello from PyCharm!"}
)

for line in response.iter_lines():
    if line:
        print(line.decode())
```

Available models can be found here:
https://registry.ollama.ai/search

To download other models:
```http
POST http://localhost:11434/api/pull
Content-Type: application/json

{
  "name": "mistral"
}
```

For more info on the REST API definition: https://github.com/ollama/ollama/blob/main/docs/api.md

