# Docker Compose

Docker compose is a handy way to run docker with configuration files.
This is nice when you have more complex containers to run, and its a difficult to type all the config
every time you want to run it.

*Important step:* Make sure you have the latest version (currently V2).

Docker compose V1 was built on python, V2 is built in Go. If you run ``which docker compose``
and it shows the path ``/usr/bin/docker-compose`` then you still have V1. Remove it
with ``sudo rm /usr/bin/docker-compose``.

Create a ``docker-compose.yaml`` file. Here's an example:

```yaml
services: # Defines the containers (services)
  app:
    image: my_flask_app:latest  # Use an existing image
    build: ..  # Or build from Dockerfile in the current directory
    ports:
      - "5000:5000"  # Map host port 5000 to container port 5000
    volumes:
      - ./app:/app  # Mount local folder to container folder
    environment:
      - FLASK_ENV=development  # Set environment variables
    depends_on:
      - db  # Wait for "db" service before starting

  db:
    image: postgres:15
    restart: always  # Restart if it crashes
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - pg_data:/var/lib/postgresql/data  # Persistent storage for DB

volumes:
  pg_data:  # Named volume for PostgreSQL data

```

Run container
``docker compose up -d``

Stop container
``docker compose down``

Upgrade container
``docker compose down``
``docker compose pull``
``docker compose up -d``

Restart container: ``docker compose restart``

Chain commands like ``docker compose down && docker compose up -d``