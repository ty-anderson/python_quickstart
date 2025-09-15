# Intro to Docker

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


## Docker Volumes

Files and Docker
If you need to use files for anything involving docker, you need to configure volumes.

Volumes are a mapping of the docker container file system to the host file system.

``-v /home/svr/immich:/usr/src/app/upload``

Just like port mapping, the first is host and second is container.
