# Servers

# Web Server

Known for serving over HTTP/HTTPS protocol. Typically websites, API's, web services, anything using HTTP(S).

## Proxy Server

Redirects web traffic. A sort of "middleman" server that is responsible for directing requests. 
For example, Nginx or Caddy can be hosted on a server. The proxy server program, once configured, 
will push requests to other servers. Good for load balancing, obscuring other servers IP address.
Specifically this reroutes web traffic like HTTP(S).

## File Server

A file server is a server that is like a central hub to hold files. 

Some common options:
- Samba https://hub.docker.com/r/dperson/samba for your typical file explorer-like experience.
- SFTP.
- Files over HTTPS aka cloud API's like Google Drive.

