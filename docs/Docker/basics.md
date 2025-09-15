# Common Commands
```bash
# When you find an image you want to use do
docker pull <image_name>

# To see images downloaded use
docker images

# see containers
docker ps

# run container. 
docker run image-name -d
# -d means run in detached mode so when the terminal is closed, the container continues to run

# Some containers need other info to run, which can be passed after the command
docker run --name postgres_db -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
# --name is what the container will be named
# -p is for port mapping host computer port to image port (first is host, second is container)
# -e is for adding environment variables

# stop docker container
docker stop image-name

# remove an image by name and tag
docker rmi postgres:latest
# or by container hash id
docker rmi 123456789abc

# Docker containers are their own sort of OS and SSH into it.
# to shell into the container
docker exec -it <container-name-or-id> /bin/sh
# /bin/sh is the terminal experience (shell in this case) you could do /bin/bash

# access container logs
docker logs <container name or id>

# continously showing log output
docker logs -f <container-name-or-id>

```