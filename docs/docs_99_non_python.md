# Non-Python

## Docker


## Reverse-Proxy

Reverse Proxy - software that routes traffic from one endpoint to another, or multiple others.

Examples: Nginx, Caddy

Caddy is very simple and it comes with built in certificate management through Lets Encrypt. 

```caddy
<requested-domain> {
    reverse_proxy <ip and port service is routed to>
}
```

Examples using Caddy:

Simple - proxy traffic to backend server. When requests go to example.com, it will get routed
to the this reverse proxy , which then pushes it to localhost:5000. Just be sure the DNS
records are updated to route the domain to this IP address.
```caddy
example.com {
    reverse_proxy localhost:5000
}
```

Here is Caddy as a reverse proxy doing load balancing, in a round-robin method.
```caddy
example.com {
    reverse_proxy backend1:5000 backend2:5000 backend3:5000
}
```

You can do path based proxying to serve different backends based on the url path. In this 
example ``example.com/api`` will go to one web server, while ``example.com/static`` goes to another.
```caddy
example.com {
    reverse_proxy /api backend1:5000
    reverse_proxy /static backend2:5001
    reverse_proxy /app backend3:5002
}
```

You can setup to route subdomains as well. This will retrieve an SSL certificate for all domains added.
```caddy
example.com {
    reverse_proxy localhost:3000
}

api.example.com {
    reverse_proxy localhost:4000
}
```

You can also proxy to external services.
```caddy
example.com {
    reverse_proxy https:/api.example.com
}
```

You can also configure domains to redirect to one domain. In this example all requests to 
www.example.com will be rerouted to example.com. 
```caddy
example.com www.example.com {
    reverse_proxy localhost:3000
}
```

To run Caddy:

- Download to computer
- Setup config file ``Caddyfile`` typically in ``/etc/caddy/Caddyfile``
- Start the Caddy server ``sudo systemctl start caddy``

To run in Docker:

- Create a docker-compose.yml file.
```docker-compose
services:
  caddy:
    image: caddy:latest
    container_name: caddy
    ports:
      - "80:80"        # HTTP
      - "443:443"      # HTTPS
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile   # Mount your Caddyfile
      - ./data:/data                       # Let’s Encrypt certificates
      - ./config:/config                   # Caddy configuration
    restart: unless-stopped
```

- Create your Caddyfile (make sure to create it in the same location your volume is pointed to).
```caddy
example.com {
    reverse_proxy backend:3000
}
```
- Run ``docker compose up -d`` to start the server.

Additional considerations to run in Docker:

- If you run Caddy in a docker container, ``localhost`` will be that container, due to dockers own DNS.
- If you run your web server that you're routing to in a docker container, you can use that container name
    in the caddy file config.

## Web Server


## File Server

