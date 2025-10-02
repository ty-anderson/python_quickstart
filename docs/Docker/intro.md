# Intro to Docker

## General
Docker creates and runs containers - software bundled to run on a minimal isolated linux OS on the host system.
Containers are great because they are typically very easy to install and even easier to uninstall.
Allows for reproducing environments, avoiding the "it runs on my machine" problem.
They can enhance security by isolating the host system from the system running the software.

## Why should I care about Docker?

- It is the modern way of running production programs.
- Docker is what runs cloud services. For example, if we spin up a resource in Azure, it's probably running on Docker.
- Fixes the issue of "it runs on my machine" for development (reproducible environment).
- Containers are isolated from the host machine, which makes it more secure.

**Docker is great for both development and production.**

## What is Docker?

Docker is a utility that hosts other programs in their own containers.

Think of a container like an ultra-light weight version of a virtual machine.

The difference between a VM and a container:
- VM's require allocating a chunk of a computer's hardware resources to its own kernel and OS.
- A container can share the kernel and user space.


Terms:

- Image: A copy of the software that is ready to run on docker.
- Container: An instance of an image, specific to the image that has been setup to run. More simply,
  a container is an image running on your machine. Can be turned on or off, etc.
