# Video Streaming Service

## Jellyfin

Docker compose file:
```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    user: "1000:1000"
    network_mode: 'host'
    volumes:
      - /srv/jellyfin/config:/config
      - /srv/jellyfin/cache:/cache
      - type: bind
        source: /srv/plex_media
        target: /plex_media
        read_only: true
    restart: 'unless-stopped'
    # Optional - alternative address used for autodiscovery
    environment:
      - JELLYFIN_PublishedServerUrl=https://jelly.healthfin.solutions
```

Some notes: Jellyfin requires a valid domain to be used if you want to cast to Chromecast. 
This is because Chromecast's require a valid certificate to stream from. To avoid this
you would have to install your self signed certificate onto your casting device.

Steps:

1. Host jellyfin
2. Setup Caddy to be a reverse proxy from your domain to the jellyfin IP.
3. Caddy will automatically issue a valid certificate for this allowing you to stream.


## Plex

Docker compose file:

```yaml
services:
  plex:
    container_name: plex
    image: linuxserver/plex
    environment:
      - PUID=1000           # Replace with your user ID
      - PGID=1000           # Replace with your group ID
      - VERSION=docker
      - PLEX_CLAIM=claim-fzdegAmx-S6iP68ysfp2
    volumes:
      - /srv/plex_media:/media    # Your media files
      - /srv/plex/config:/config   # Plex configuration files
    network_mode: host
    restart: unless-stopped
```

Plex does a lot of the certificate management stuff for you. You can connect
your server to the Plex system to stream, but its not quite a true self hosted
solution. After you setup your plex server you must go to Plex.com and sign up
then add your server to your account under their domain. You still end up
relying on their system. It does come with a lot of other free content through
Plex which is a benefit.

## Notes

Note that both of these require some kind of external internet to work. If you
want to truely isolated setup that will work if the internet as a whole
goes down, you will need streaming devices on your TV that can install the Jellyfin
client app. 

These include:

- NVIDIA Shield TV (best all-around).
- Cheap Android TV box (Amlogic, etc.) sideloaded with Jellyfin app.
- Intel NUC, Raspberry Pi, or old mini PC hooked up via HDMI and running Linux + Jellyfin Desktop/Browser.

