# Docker

## General
Docker creates and runs containers - software bundled to run on a minimal isolated linux OS on the host system.
Containers are greate because they are typically very easy to install and even easier to uninstall. 
Allows for reproducing environments, avoiding the "it runs on my machine" problem.
They can enhance security by isolating the host system from the system running the software.

Terms:
- Image: A copy of the software that is ready to run on docker.
- Container: An instance of an image, specific to the image that has been setup to run. More simply, 
a container is an image running on your machine. Can be turned on or off, etc.
- Volume: A path that a container can use to access host file system.

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

Remove an image by name and tag: ``docker rmi postgres:latest`` or by image id ``docker rmi 123456789abc``


## Access Docker Container

Access the container environment ``docker exec -it <container-name-or-id> /bin/sh``
/bin/sh is the terminal experience (shell in this case) you could do /bin/bash

Access container logs
``docker logs <container name or id>``

For continuously showing log output
``docker logs -f <container-name-or-id>``

## Docker Volumes

Files and Docker
If you need to use files for anything involving docker, you need to configure volumes.

Volumes are a mapping of the docker container file system to the host file system.

``-v /home/svr/immich:/usr/src/app/upload``

Just like port mapping, the first is host and second is container.
