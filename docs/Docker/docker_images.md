# Build a Docker Image

A **Dockerfile** is how to build an image. The contents might look something like this:

Simple python app:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Flask app:
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

When your dockerfile is ready, run: ``docker build -t my-image-name:tag .``

• Replace my-image-name with the name you want to give your image.
• Replace tag with an optional version (e.g., latest or v1.0).

End example might look like ``docker build -t my-flask-app:latest .``

If you are building on a Mac, but will run on Linux, when you build an image, specify to run on amd64:
``docker build --platform linux/amd64 -t yt_download:latest .``

Save the image to a tar file:
``docker save -o /Users/tyleranderson/Downloads/yt_downloads_250226.tar yt_download:latest``

Load the file as an image: ``docker load -i /srv/flask_yt_download/yt_downloads_250226.tar``

## Docker Compose with Custom Images

When you use docker compose with an image, you have two options:

- To build the image with docker compose when its run, use the ``build: .`` option.
  This builds the image from the Dockerfile in the directory.
```yaml
services:
  flask_app:
    build: .  # This tells Compose to use the Dockerfile in the current directory
    container_name: flask_gunicorn
    ports:
      - "8090:8090"

```
- If you already built the image with ``docker build -t myflaskapp:latest .`` then you can tell docker compose
  what image to use:
```yaml
services:
  flask_app:
    image: my_flask_app  # Use the existing built image
    container_name: flask_gunicorn
    ports:
      - "8090:8090"

```

## Docker Image Files

Save image to file:
``docker save -o /path/to/destination/image-name.tar my-image-name:tag``

Load image from file:
``docker load -i /path/to/destination/image-name.tar``