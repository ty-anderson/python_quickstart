# Caddy

Official site: https://caddyserver.com/

docker compose:
```yaml
services:
  caddy:
    image: caddy:latest
    container_name: caddy
    ports:
      - "80:80"        # HTTP
      - "443:443"
      - "8009:8009"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile   # Mount your Caddyfile
      - ./data:/data                       # Let’s Encrypt certificates
      - ./config:/config                   # Caddy configuration
      - /srv/web_apps/notes:/srv/web_apps/notes
    restart: unless-stopped
```

Don't forget to open the port(s) in the firewall.

## Reverse-Proxy

Reverse Proxy - software that routes traffic from one endpoint to another, or multiple others.

Caddy is very simple and it comes with built in certificate management through Lets Encrypt. 

```nginx
<requested-domain> {
    reverse_proxy <ip and port service is routed to>
}
```

### Examples using Caddy:

Very simple config. This says using the host machine ip address, using the protocol on port 80 (http)
respond with "Hello from Caddy".

```nginx
:80 {
    respond "Hello from Caddy"
}
```

Internal and localhost certificates
If you configure sites with local or internal addresses, Caddy will serve them over HTTPS 
using a locally-trusted certificate authority with short-lived, auto-renewing certificates. 
It even offers to install your unique root into your local trust stores for you.
```nginx
localhost {
	respond "Hello from HTTPS!"
}

192.168.1.10 {
	respond "Also HTTPS!"
}

http://localhost {
	respond "Plain HTTP"
}
```

When requests go to example.com, it will get routed
to this reverse proxy, which then pushes it to localhost:5000. Just be sure the DNS
records are updated to route the domain to this IP address.
```nginx
example.com {
    reverse_proxy localhost:5000
}
```

Here is Caddy as a reverse proxy doing load balancing, in a round-robin method.
```nginx
example.com {
    reverse_proxy backend1:5000 backend2:5000 backend3:5000
}
```

You can do path based proxying to serve different backends based on the url path. In this 
example ``example.com/api`` will go to one web server, while ``example.com/static`` goes to another.
```nginx
example.com {
    reverse_proxy /api backend1:5000
    reverse_proxy /static backend2:5001
    reverse_proxy /app backend3:5002
}
```

You can setup to route subdomains as well. This will retrieve an SSL certificate for all domains added.
```nginx
example.com {
    reverse_proxy localhost:3000
}

api.example.com {
    reverse_proxy localhost:4000
}
```

You can also proxy to external services.
```nginx
example.com {
    reverse_proxy https:/api.example.com
}
```

You can also configure domains to redirect to one domain. In this example all requests to 
www.example.com will be rerouted to example.com. 
```nginx
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
```yaml
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
```nginx
example.com {
    reverse_proxy backend:3000
}
```
- Run ``docker compose up -d`` to start the server.

Additional considerations to run in Docker:

- If you run Caddy in a docker container, ``localhost`` will be that container, due to dockers own DNS.
- If you run your web server that you're routing to in a docker container, you can use that container name
    in the caddy file config.

You can also route ports directly.

```nginx
:8443 {
    reverse_proxy 127.0.0.1:8000
}
```

## File Server

Caddy has an option to serve static files over HTTP. This is not a file server like sFTP
because it serves over http or https.

```nginx
healthfin.solutions {
    root * /srv/website
    file_server
}
```

Serve different sites with different paths of the same domain.

```nginx
healthfin.solutions {
    handle_path /notes* {
        root * /srv/web_apps/notes
        file_server
    }

    reverse_proxy homeserver.home:8000
}

:8009 {
    root * /srv/web_apps/notes
    file_server
}
```

This config allows for access to the main server from the root domain, but 
also changes to the static site when you add the /notes path.

Don't forget you can setup a local DNS server on your machine and setup a 
local domain DNS rewrite.

```nginx
anderson.docs {
    tls internal
    root * /srv/web_apps/notes
    file_server
}
```
