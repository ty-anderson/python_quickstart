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

## Docker Compose Build on Run

When you use docker compose with an image, you have two options:

1. Build the image on run.
2. Run from an existing image.

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