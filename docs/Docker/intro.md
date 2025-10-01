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
