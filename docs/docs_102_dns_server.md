# DNS Server

A DNS Server is a server that holds domain name records and point to the 
corresponding IP addresses. 

## Adguard

You can setup your own local DNS server on your network. Frequently these
allow you to setup your own name resolutions on your network, but also block
certain sites from resolving, which can prevent ads.

## Concept 1

You can setup your own DNS server on your network. Open source servers include
adguard, dnsmasq, and pihole. 

<div class="mermaid">
graph TD
    A[Router]
    B[Internet]
    C[Home Server]
    D[Computer 1]
    E[Computer 2]

    B <-..-> A
    C --Otherwise have your router use its default DNS--> A
    D --Resolve DNS Here First--> C
</div>

## Options

You have two options when setting up your own DNS server

1. Set up individual devices on your network to use self-hosted DNS server
2. Set up your router to point all devices to the self-hosted DNS server.

## Setup Adguard

Docker compose file:

```docker
services:
  adguardhome:
    container_name: adguardhome
    image: adguard/adguardhome
    restart: unless-stopped
    ports:
      - "53:53/udp"
      - "53:53/tcp"
      - "3000:80/tcp"   # Web UI
#      - "443:443/tcp" # (Optional, for HTTPS UI)
    volumes:
      - ./workdir:/opt/adguardhome/work
      - ./confdir:/opt/adguardhome/conf
```

``sudo docker compose up -d`` - you now have a DNS server running.

To access the web UI you can go to ``http://<ip address>:3000``.

To add a local domain, go to Filters>DNS rewrites

If you want to do option 1:

Go to the device(s) you want to use your DNS server. Go to System Preferences ->
Network -> Wifi (or Ethernet) -> DNS. From there add the IP address of your 
server running the DNS server.

If you want option 2:

Go into your router options. Find DNS settings (might be under DHCP Settings).

Add your custom server, its a good idea to add a fallback server in case yours
goes down. Google is 8.8.8.8 or cloudflare 1.1.1.1.


