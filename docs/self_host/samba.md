# Shared File Server

Samba is an open source file server. You can host a network drive
to share files across different computers.

You can dictate account creations, read/write access. You can create
multiple shared folders and assign access to each. This means you
could have a share one for people to maybe download photos from
but keep a private one for your own files you don't want to share.

**Warning:** There are several different versions of samba, some are older 
and have bugs. The version below is current as of 2025-10-24.

Here is a good config. It does the following:

- Uses .env file for user creds.
- Mounts several different directories for managing public/private access.
- Allows a guest to view files without any creds.

```yaml
services:
  samba:
    image: ghcr.io/servercontainers/samba:latest
    container_name: samba
    restart: unless-stopped

    # --- SMB port ---
    ports:
      - "445:445"            # SMB direct (modern clients only)

    # --- Host folders mapped into container ---
    volumes:
      - /srv/plex_media:/mount/media
      - /srv/samba_file_share/shared_private:/mount/shared_private
      - /srv/samba_file_share/shared_public:/mount/shared_public

    # --- User and share definitions ---
    environment:
      # --- Create the admin account ---
      ACCOUNT_tyler: "${ADMIN_PASS}"     # user=tyler, password from .env or defaults to 'changeme'
      UID_tyler: 1000                              # match your host user ID if you like

      # --- MEDIA share (authenticated only) ---
      SAMBA_VOLUME_CONFIG_Media: >
        [Media];
        path = /mount/media;
        read only = no;
        browsable = yes;
        guest ok = no;
        valid users = tyler;
        create mask = 0666;
        directory mask = 0777

      # --- PRIVATE share (authenticated only) ---
      SAMBA_VOLUME_CONFIG_Private: >
        [Private];
        path = /mount/shared_private;
        read only = no;
        browsable = yes;
        guest ok = no;
        valid users = tyler;
        create mask = 0666;
        directory mask = 0777

      # --- PUBLIC share (guest access allowed) ---
      SAMBA_VOLUME_CONFIG_Public: >
        [Public];
        path = /mount/shared_public;
        read only = no;
        browsable = yes;
        guest ok = yes;
        public = yes;
        available = yes;
        create mask = 0666;
        directory mask = 0777

    # Optional logging/diagnostics
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Connect Other Computers

There are two methods of connecting to a samba shared drive.

1. Session based (temporary logged).
2. Auto mount (stays logged in).

To connect your other computers to the shared drive.

### Mac

**Temporary login:**

- In Finder, select Go from the drop down menu.
- Select "Connect to a Server".
- Enter the SMB path like ``smb://<server-ip>/Media`` or ``smb://<server-ip>/Private``
- Click "Connect".
- Enter credentials.

**Full auto-mount login:**

If you prefer the graphical route:

- Mount the shares once manually in Finder (⌘ + K → connect)
- Open System Settings → Users & Groups → Login Items
- Under Open at Login, click +
- Select your mounted share(s)

They’ll automatically connect when you log in.


### Windows

- Open File Explorer
- Right-click **This PC** → **Map network drive…**
- Assign a drive letter. Choose a letter (for example `M:` for Media, `P:` for Private).
- Enter the network path For example:

```
\\192.168.1.50\Media
```

or

```
\\192.168.1.50\Private
```

- Authentication
  * For the **Media** share: check “Connect using different credentials” and log in as **guest** (no password).
  * For the **Private** share: log in as `tyler` with your Samba password.
- Check **“Reconnect at sign-in”** — Windows will mount these every time you log in.
