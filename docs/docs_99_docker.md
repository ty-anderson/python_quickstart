## Docker

Docker uses images of a software to create containers that run them. They will create their own isolated environment on the host system. They are typically very easy to install and even easier to uninstall. They can enhance security by isolating the host system from the system running the software.

When you find an image you want to use do:
``docker pull <image_name>``

To see images downloaded use:
``docker images``

See containers:
``docker ps``

Run container:
``docker run image-name -d``
-d means run in detached mode so when the terminal is closed, the container continues to run

Some containers need other info to run, which can be passed after the command:
Postgres example:
``docker run --name postgres_db -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres``

- --name is what the container will be named
- -p is for port mapping host computer port to image port (first is host, second is container)
- -e is for adding environment variables


### Docker Compose

Make sure you have the latest version (currently V2).

Docker compose V1 was built on python, V2 is built in Go. If you run ``which docker compose`` 
and it shows the path ``/usr/bin/docker-compose`` then you still have V1. Remove it
with ``sudo rm /usr/bin/docker-compose``. 

Docker compose is a handy way to run docker with certain settings in a yaml file
Create a docker-compose.yaml file.

Run container
``docker compose up -d``

Stop container
``docker compose down``

Upgrade container
``docker compose down``
``docker compose pull``
``docker compose up -d``


### Build a Docker Image

A Dockerfile is how to build an image. The contents might look something like this:

*Dockerfile*
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

When your dockerfile is ready, run:
``docker build -t my-image-name:tag .``

• Replace my-image-name with the name you want to give your image.
• Replace tag with an optional version (e.g., latest or v1.0).

Save image to file:
``docker save -o /path/to/destination/image-name.tar my-image-name:tag``

Load image from file:
``docker load -i /path/to/destination/image-name.tar``


Access docker container in terminal
Access the container environment
``docker exec -it <container-name-or-id> /bin/sh``

/bin/sh is the terminal experience (shell in this case) you could do /bin/bash


Access container logs
``docker logs <container name or id>``

For continuously showing log output
``docker logs -f <container-name-or-id>``

Files and Docker
If you need to use files for anything involving docker, you need to configure volumes.

Volumes are a mapping of the docker container file system to the host file system.

``-v /home/svr/immich:/usr/src/app/upload``

Just like port mapping, the first is host and second is container.


