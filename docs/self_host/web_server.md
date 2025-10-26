# Web Servers

A web server is a server that serves data over the HTTP/HTTPS protocols.
Typically it is HTML, JSON, XML, or some other type of data. 

## Reverse Proxy

A reverse proxy is a process that will reroute network traffic that flows
through the HTTP/HTTPS protocols, to other machines, using IP addresses.
One example is if you setup a proxy server to take any networks requests
to the public ip address A, it will take those requests and push them to
the machine with local ip address B.

Think of it like a concierge for your website. You have a website welcome.com.
When someone goes to welcome.com, the public DNS will use that name to go to
the public IP you configured, and then when the traffic reaches your server,
your concierge takes them to the correct room (machine).

## Caddy

Caddy is a very easy web server/reverse proxy. It handles certificate creation
automatically which is super helpful. It also can be used to distribute traffic
for load balancing, serve static web files, handle simple auth, and more.

The way you setup caddy is with docker compose:

## Docker Compose

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
      - /srv/web_apps:/srv/web_apps        # custom directory I want caddy to have access to for static web pages
    dns:
      - 1.1.1.1
      - 8.8.8.8
    restart: unless-stopped
```

## Caddyfile

Once the server is running, the caddyfile is the base config for what you want it
to do. Create a file called ``Caddyfile`` and then update based on what you want.
Here are the offical docs: https://caddyserver.com/docs/caddyfile

Basic File:
```caddyfile
localhost {
	respond "Hello, world!"
}

localhost:2016 {
	respond "Goodbye, world!"
}
```

## Certificates

Using certain names in your caddyfile have important caveats. For example, LetsEncrypt,
the certificate authority that Caddy uses will not issue certificates for localhost. 
They only do for public domains. Also your browser will show a "Not Trusted" message
when you try to go to it. 

You can get a local cert program like mkcert and set that up.

Caddy has a self signed cert with TLS. You can use this like below:

```caddyfile
localhost {
    root * /srv/web_apps/dev_site
    file_server
    tls internal
}
```

## Authentication

You can add basic HTTP authentication to any of your routes. Use bcrypt
to generate a password hash like 

```bash
# with caddy
caddy hash-password --plaintext "yourpassword"

# docker
sudo docker exec -it caddy caddy hash-password --plaintext "yourpassword"
```

Then add your auth to your route in Caddyfile.
```caddyfile
# add auth to entire site
yourdomain.com {
    basicauth {
        user password_hash
    }

    root * /srv/web_apps/site
    file_server
}

# add auth to specific route
example.com {
    handle /admin* {
        basicauth {
            user password_hash
        }
        root * /srv/web_apps/admin
        file_server
    }

    handle / {
        root * /srv/web_apps/public
        file_server
    }
}
```

## Full File
```caddyfile
(basic_auth_users) {
    @protected {
        not path /public_notes*   # everything EXCEPT /public_notes*
    }

    basic_auth @protected  {
            user password_hash
        }
    }

home.server {
    tls internal

    handle / {
        root * /srv/web_apps/home
        file_server
    }

    handle /test* {
        respond "Hello from test path"
    }

    handle /notes* {
        root * /srv/web_apps
        file_server browse
    }

    handle {
        respond "❌ Unmatched path: {uri}" 404
    }
}


healthfin.solutions {
    handle /public_notes* {
            root * /srv/web_apps
            file_server
        }

    import basic_auth_users

    handle / {
        root * /srv/web_apps/home
        file_server
    }

    handle /confetti {
        rewrite * /confetti.html
        root * /srv/web_apps/home
        file_server
    }

    handle /timeline {
        rewrite * /timeline.html
        root * /srv/web_apps/home
        file_server
    }

    handle /notes* {
            root * /srv/web_apps
            file_server
        }

    handle {
        respond "❌ Unmatched path: {uri}" 404
    }
}


# billboard analytics
billboard.anderson {
    tls internal
    reverse_proxy 192.168.1.104:8000
}

billboard.healthfin.solutions {
    import basic_auth_users

    reverse_proxy 192.168.1.104:8000 {
        header_up Host {http.request.host}  # fixes the issue of static files in the website.
    }
}

# immich
pics.anderson {
    tls internal
    reverse_proxy 192.168.1.104:2283
}

pics.healthfin.solutions {
    import basic_auth_users

    reverse_proxy 192.168.1.104:2283 {
        header_up Host {http.request.host}  # fixes the issue of static files in the website.
    }
}

# LLM
ollama.anderson {
    tls internal
    reverse_proxy 192.168.1.104:3001
}

ai.healthfin.solutions {
    reverse_proxy 192.168.1.104:3001
}

yt.healthfin.solutions {
    import basic_auth_users
    reverse_proxy 192.168.1.104:8091
}

jelly.healthfin.solutions {
    reverse_proxy 192.168.1.104:8096
}

docs.anderson {
    tls internal
    root * /srv/web_apps/notes
    file_server
}

dns.anderson {
    import basic_auth_users
    tls internal
    reverse_proxy 192.168.1.104:3000
}

resources.anderson {
    import basic_auth_users
    tls internal
    reverse_proxy 192.168.1.104:19999
}

jdownloader.anderson {
    import basic_auth_users
    tls internal
    reverse_proxy 192.168.1.104:5800
}

torrent.anderson {
    import basic_auth_users
    tls internal
    reverse_proxy 192.168.1.104:8080
}

```