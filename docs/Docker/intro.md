# Intro to Docker

## General
Docker creates and runs containers - software bundled to run on a minimal isolated linux OS on the host system.

## Why should I care about Docker?

- It is the modern way of running production programs.
- Docker is what runs cloud services. For example, if we spin up a resource in Azure, it's probably running on Docker.
- Fixes the issue of "it runs on my machine" for development (reproducible environment).
- Containers are isolated from the host machine, which makes it more secure.
- Great for both development and production.
- Very easy to install and uninstall programs.
- **Extremely stable and reproducible environments.**

## What is Docker?

Docker is a utility that hosts other programs in their own containers. 
Think of a container like an ultra-light weight version of a virtual machine.

The difference between a VM and a container:

- VM's require allocating a chunk of a computer's hardware resources to its own kernel and OS.
- A container can share the kernel and user space.
