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

# view docker resource usage
docker stats

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

Files and Docker: 

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